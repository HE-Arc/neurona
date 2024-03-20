from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

from neuronaApp.models import ApiKeys


class TokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.META.get("HTTP_AUTHORIZATION")

        if not token:
            raise AuthenticationFailed("Token not provided")

        try:
            token = ApiKeys.objects.get(key=token)

        except ApiKeys.DoesNotExist:
            raise AuthenticationFailed("Invalid token")

        if token.has_expired():
            token.delete()
            raise AuthenticationFailed("Token has expired")

        return token.user, token