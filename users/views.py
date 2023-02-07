from django.shortcuts import render
from rest_framework.response import responses
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from .serializers import UserCreateSerializer,UserLoginSerializer
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

# Create your views here.

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer


class UserLoginAPIView(APIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        my_data = request.data
        serializer = UserLoginSerializer(data=my_data)
        if serializer.is_valid(raise_exception=True):
            valid_data = serializer.data
            return responses(valid_data, status=HTTP_200_OK)
        return responses(serializer.errors, HTTP_400_BAD_REQUEST)





