from django.contrib import admin

# Register your models here.
from .models import User,Registratsiya,Product

admin.site.register(Registratsiya)
admin.site.register(User)
admin.site.register(Product)