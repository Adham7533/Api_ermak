from rest_framework import serializers
from .models import User,Registratsiya,Product


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name',
                  'last_name',
                  'fuls_name',
                  'phone',
                  'oil',
                  'email',
                  'id']
class RegistratsiyaSerializers(serializers.ModelSerializer):
    class Meta:
        model=Registratsiya
        fields=[
            'id',
            'name',
            'phone',
            'email',
            'status'
        ]


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=[
            'title',
            'keywords',
            'register'
        ]