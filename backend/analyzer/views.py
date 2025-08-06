import re
import json
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

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
        result = Ventureviz().crew().kickoff(inputs={"domain": domain})

        if isinstance(result, str):
            # Check if result is a string wrapped with ```json ... ```
            match = re.search(r"```json\n(.*?)\n```", result, re.DOTALL)    # Match and extract JSON content inside ```json ... ```
            if match:
                clean_json = match.group(1)
                
                try:
                    parsed = json.loads(clean_json)
                    return JsonResponse(parsed, safe=False)
                except json.JSONDecodeError:
                    return JsonResponse({"error": "Invalid JSON inside backticks"}, status=500)
            else:
                return JsonResponse({"error": "Expected JSON block not found in result"}, status=500)

        # If result is a valid JSON-compatible dict already
        elif isinstance(result, dict):
            return JsonResponse(result, safe=False)

        # If result has `.model_dump()`, like a Pydantic object
        elif hasattr(result, "model_dump"):
            return JsonResponse(result.model_dump(), safe=False)

        return JsonResponse({"error": "Unsupported result format"}, status=500)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)