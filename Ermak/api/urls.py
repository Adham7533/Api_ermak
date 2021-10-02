from django.urls import path
from . import views
from api.serializers import UserSerializers

urlpatterns=[
    path('user/',views.UserApiView.as_view()),
    path('register/',views.RegistratsiyaApiView.as_view()),
    path('product/',views.ProductApiView.as_view()),
]