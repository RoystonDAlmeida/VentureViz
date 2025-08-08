import re
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from analyzer.models import AnalysisResult

# Import your Crew class
from ventureviz.crew import Ventureviz

@csrf_exempt
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

    try:
        data = json.loads(request.body)
        domain = data.get("domain")
        if not domain:
            return JsonResponse({"error": "Missing 'domain' in request body"}, status=400)

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