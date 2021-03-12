#!/usr/bin/env python3
# -*-encoding: utf-8-*-

import jwt
from django.conf import settings
from rest_framework import authentication, exceptions
from .models import User


class JWTAuthentication(authentication.BaseAuthentication):
    authentication_header_prefix = 'Token'

    def authenticate(self, request):
        """
        The authenticate method is called every time, regardless of whether it requires
        whether the endpoint of the authentication. 'authenticate' has two possible
        return values:
            1) None - we return None if we don't want to authenticate.
            This usually means that we mean that authentication will fail.
            An example of this is, for example, the case where the token is not included in
            title.
            2) (user, token) - we return user / token combination
            when authentication is successful. If none of
            cases are not met, this means that an error has occurred, and we
            we do not return anything. In this case, we will simply throw an exception.
            AuthenticationFailed and let DRF do the rest.
        """
        request.user = None

        # 'auth_header' must be an array with two elements:
        # 1) by the name of the authentication header (Token in our case)
        # 2) the JWT itself, by which we must authenticate
        auth_header = authentication.get_authorization_header(request).split()
        auth_header_prefix = self.authentication_header_prefix.lower()

        if not auth_header:
            return None

        if len(auth_header) == 1:
            # Incorrect token header, one element passed in the header
            return None

        elif len(auth_header) > 2:
            # Incorrect token header, some extra whitespace characters
            return None

        # The JWT library we are using usually handles incorrectly
        # the bytes type, which is commonly used by the standard libraries
        # Python3 (HINT: use PyJWT). To solve this exactly, we need
        # decode prefix and token. This is not the cleanest code, but it is good
        # solution because there might be a mistake, we don't.
        prefix = auth_header[0].decode('utf-8')
        token = auth_header[1].decode('utf-8')

        if prefix.lower() != auth_header_prefix:
            # Header prefix is not what we expected - failure.
            return None

        # At this point, there is a "chance" that authentication will succeed.
        # We are delegating the actual authentication of the credentials to the method below.
        return self._authenticate_credentials(request, token)

    def _authenticate_credentials(self, request, token):
        """
       Attempting to authenticate with the provided data. If successful -
         return user and token, otherwise - throw an exception.
        """
        try:
            payload = jwt.decode(token, settings.SECRET_KEY)
        except Exception:
            msg = 'Authentication error. Unable to decode token'
            raise exceptions.AuthenticationFailed(msg)

        try:
            user = User.objects.get(pk=payload['id'])
        except User.DoesNotExist:
            msg = 'No user matching this token was found.'
            raise exceptions.AuthenticationFailed(msg)

        if not user.is_active:
            msg = 'This user has been deactivated.'
            raise exceptions.AuthenticationFailed(msg)

        return (user, token)
