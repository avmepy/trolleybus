from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.serializers import RegistrationSerializer, LoginSerializer, UserSerializer
from accounts.renderers import UserJSONRenderer


class RegistrationAPIView(APIView):
    """
    Allow all users (authenticated and not) access to this endpoint.
    """
    permission_classes = AllowAny,
    serializer_class = RegistrationSerializer
    renderer_classes = UserJSONRenderer,

    def post(self, request):
        user = request.data.get('user', {})

        # Serializer creation, validation and persistence pattern
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = LoginSerializer

    def post(self, request):
        user = request.data.get('user', {})

        # Note that we do not call the save() method of the serializer like
        # did it for registration. The fact is that in this case we
        # nothing to save. Instead, the validate() method does the right thing.
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        # There is nothing to validate or save here. We just want to
        # the serializer handled converting the User object to something that
        # can be cast to json and returned to the client.
        serializer = self.serializer_class(request.user)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        serializer_data = request.data.get('user', {})

        # The pattern of serialization, validation and persistence
        serializer = self.serializer_class(
            request.user, data=serializer_data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)
