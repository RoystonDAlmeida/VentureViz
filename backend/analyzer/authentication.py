from firebase_admin import auth
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from django.contrib.auth.models import User

class FirebaseAuthentication(BaseAuthentication):
    def authenticate(self, request):
        """
        Authenticate a user based on a Firebase ID token in the request headers.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:    
            tuple: A tuple containing the authenticated user and None.
        """
        
        id_token = request.headers.get('Authorization')

        if not id_token:
            return None

        if id_token.startswith("Bearer "):
            id_token = id_token.split("Bearer ")[1]

        try:
            decoded_token = auth.verify_id_token(id_token)
        except Exception:
            raise exceptions.AuthenticationFailed('Invalid Firebase ID token.')

        uid = decoded_token.get('uid')
        email = decoded_token.get('email')

        if not email:
            raise exceptions.AuthenticationFailed('No email found in Firebase token.')

        # Get or create Django user linked to Firebase UID
        user, created = User.objects.get_or_create(username=uid, defaults={"email": email})
        return (user, None)
