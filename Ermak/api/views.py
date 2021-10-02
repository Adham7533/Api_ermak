from django.shortcuts import render
from .serializers import UserSerializers,RegistratsiyaSerializers,Product
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .models import User,Registratsiya


# Create your views here.

class UserApiView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers

class RegistratsiyaApiView(generics.ListCreateAPIView):
    queryset = Registratsiya.objects.all()
    serializer_class = RegistratsiyaSerializers
    def slug(self,*args,data):
        pass

class ProductApiView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = RegistratsiyaSerializers