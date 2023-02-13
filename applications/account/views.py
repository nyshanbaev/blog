from django.shortcuts import render
from rest_framework.views import APIView
from applications.account.serializers import RegisterSerializers, LoginSerializer
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

User = get_user_model()
class RegisterAPIView(APIView):
    def post(self, request):
        serializer = RegisterSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # RegisterSerializers()

        return Response('Registration is ok. You have email with activation code', status=201)

class ActivationView(APIView):
    def get(self, request, activation_code):
        try:
            user = User.objects.get(activation_code=activation_code)
            user.is_active = True
            user.activation_code = ''
            user.save()
            return Response('Успешно', status=200)
        except User.DoesNotExist:
            return Response('Link expired', status=400)


class LoginAPIView(ObtainAuthToken):
    serializer_class = LoginSerializer
class LogoutAPIView(ObtainAuthToken):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            user = request.user
            Token.objects.get(user=user).delete()
            return Response('LOGOUT!!!', status=200)
        except:
            return Response('ERROR', status=403)