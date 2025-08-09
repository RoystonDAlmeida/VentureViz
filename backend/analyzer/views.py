import re
import json
from datetime import timedelta
from django.utils import timezone
from django.http import JsonResponse
from analyzer.models import AnalysisResult, UserRequestLog

# Import your Crew class
from ventureviz.crew import Ventureviz

# DRF imports
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import AllowAny

# Custom firebase authentication import
from analyzer.authentication import FirebaseAuthentication

def get_client_ip(request):
    """Extract real IP address from request, including behind proxy."""

    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0].strip()
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip

@api_view(['POST'])
@authentication_classes([FirebaseAuthentication])
@permission_classes([AllowAny])  # Allow both auth and anon users
def analyze_domain(request):
    """
        @Description:- Analyze a domain using the Ventureviz Crew.
        @Args:
            request:- The HTTP request object.
        @Returns:
            JsonResponse:- A JSON response containing the analysis results.
    """

    if request.method != "POST":
        return JsonResponse({"error": "Only POST allowed"}, status=405)

    # Extract the user and get the domain
    user = request.user
    domain = request.data.get("domain")

    if not domain:
        return JsonResponse({"error": "Missing 'domain' in request body"}, status=400)

    # 🔐 Limit anonymous users to 2 requests
    if not user or not user.is_authenticated:
        ip = get_client_ip(request)
        now = timezone.now()
        cutoff = now - timedelta(hours=24)

        # Count number of requests from this IP in the last 24h
        recent_requests = UserRequestLog.objects.filter(ip_address=ip, timestamp__gte=cutoff).count()

        if recent_requests >= 2:
            return JsonResponse({"error": "Request limit reached. Please sign up or log in."}, status=403)

        # Log this request
        UserRequestLog.objects.create(ip_address=ip)

    # 🧠 Run CrewAI
    try:
        # Run the crew with the provided domain(Response is raw text output)
        crew_output = Ventureviz().crew().kickoff(inputs={"domain": domain})

        # Extract the raw output of the crew
        raw_crew_output_str = crew_output.raw

        if isinstance(raw_crew_output_str, str):
            # Check if result is a string wrapped with ```json ... ```
            match = re.search(r"```json\n(.*?)\n```", raw_crew_output_str, re.DOTALL)    # Match and extract JSON content inside ```json ... ```
            if match:
                crew_result_json_str = match.group(1)

                try:
                    crew_result_json_dict = json.loads(crew_result_json_str)
                    
                    startup_list = crew_result_json_dict.get("startup_list", [])
                    if startup_list:
                        # Verify that startup_list is not None
                        try:
                            # Create an ORM record of ORM class "AnalysisResult"
                            AnalysisResult.objects.create(
                                domain=domain,
                                user=user if user.is_authenticated else None,
                                startup_list=crew_result_json_dict.get("startup_list", []),
                                trends_analysis=crew_result_json_dict.get("trends_analysis", ""),
                                investment_summary=crew_result_json_dict.get("investment_summary", "")
                            )
                
                        except Exception as e:
                            return JsonResponse({"error": str(e)}, status=500)

                    return JsonResponse(crew_result_json_dict, safe=False)
                            
                except json.JSONDecodeError:
                    return JsonResponse({"error": "Invalid JSON inside backticks"}, status=500)
            else:
                return JsonResponse({"error": "Expected JSON block not found in result"}, status=500)

        # If result is a valid JSON-compatible dict already
        if isinstance(raw_crew_output_str, dict):
            return JsonResponse(raw_crew_output_str, safe=False)

        return JsonResponse({"error": "Unsupported result format"}, status=500)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)