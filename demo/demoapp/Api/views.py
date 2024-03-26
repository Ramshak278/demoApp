from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK
from rest_framework_simplejwt.views import TokenViewBase

from .serializers import RegisterDataSerializer, RegisterSerializer, TokenObtainPairSerializer, UserSerializer
from ..Helpers import get_token_for_user


class Registrations(CreateAPIView):
    permission_classes = [AllowAny,]
    serializer_class = RegisterDataSerializer
    def post(self,request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        payload = get_token_for_user(user)
        userData = UserSerializer(user)
        responseData={**userData.data,"Token":payload['access']}
        return Response(responseData,status=HTTP_201_CREATED)

class MyTokenObtainPairView(TokenViewBase):
    serializer_class = TokenObtainPairSerializer

class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    def get(self, request, *args, **kwargs):
        user=request.user
        serializer=self.serializer_class(user)
        return Response(serializer.data,status=HTTP_200_OK)

