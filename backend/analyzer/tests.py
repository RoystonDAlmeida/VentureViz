import json
from django.test import TestCase, Client
from django.urls import reverse
from unittest.mock import patch

class AnalyzeDomainTests(TestCase):
    def setUp(self):
        """
            @Description:-
                        Special method that runs before every test function in the class
        """

        self.url = reverse("analyze")

        # Create a dummy web browser client to make HTTP requests
        self.client = Client()

        # Define a valid payload
        self.valid_payload = {"domain": "healthcare"}

    @patch("ventureviz.crew.Ventureviz.crew")
    def test_post_analyze_valid_domain(self, mock_crew):
        """
            @Description:-
                        Test the POST /analyze endpoint with a valid domain
        """

        # Simulate the expected JSON response your crew would return
        mock_crew.return_value.kickoff.return_value = {
            "startup_list": [{"name": "Test Startup", "description": "Desc", "website": "test.com"}],
            "trends_analysis": "Healthcare is trending...",
            "investment_summary": "# Summary\n\nVC brief..."
        }

        # This domain triggers your crew
        response = self.client.post(
            "/analyze",
            data=json.dumps(self.valid_payload),
            content_type="application/json"
        )

        self.assertEqual(response.status_code, 200)

        response_data = response.json()

        # Validate whether the keys are present in the response
        # Expected keys: 'startup_list', 'trends_analysis', 'investment_summary'
        self.assertIn("startup_list", response_data)
        self.assertIn("trends_analysis", response_data)
        self.assertIn("investment_summary", response_data)

    def test_post_analyze_missing_domain(self):
        """
            @Description:-
                        Test the POST /analyze endpoint with a missing domain
        """

        response = self.client.post(
            "/analyze",
            data=json.dumps({}),
            content_type="application/json"
        )

        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json())

    def test_non_post_method(self):
        """
            @Description:-
                        Test the POST /analyze endpoint with a non-POST method(GET method)
        """

        response = self.client.get("/analyze")
        self.assertEqual(response.status_code, 405)
        self.assertIn("error", response.json())