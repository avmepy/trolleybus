from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.serializers import RegistrationSerializer


class RegistrationAPIView(APIView):
    """
    Allow all users (authenticated and not) access to this endpoint.
    """
    permission_classes = AllowAny,
    serializer_class = RegistrationSerializer

    def post(self, request):
        user = request.data.get('user', {})

        # Serializer creation, validation and persistence pattern
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)