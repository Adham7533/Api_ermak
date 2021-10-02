from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    fuls_name = models.CharField(max_length=255, blank=True)
    phone = PhoneNumberField()
    oil = models.IntegerField(blank=False)
    email = models.EmailField('Email', max_length=255, blank=True)

    def __str__(self):
        return self.name


class Registratsiya(models.Model):
    STATUS = (
        ('Toshkent', 'Toshkent'),
        ('Samarqand', 'Samarqand'),
        ('Jizzax', 'Jizzax'),
        ('Fargona', 'Fargona'),
        ('Suexandaryo', 'Suexandaryo'),
        ('Andijon', 'Andijon'),
        ('Namangan', 'Namangan'),
        ('Navoiy', 'Navoiy'),
    )
    name = models.CharField(max_length=255, blank=True)
    phone = PhoneNumberField()
    email = models.EmailField('Email', max_length=255, blank=True)
    status = models.CharField(max_length=255, blank=False, choices=STATUS)

    def __str__(self):
        return self.name


class Product(models.Model):
    register = models.ForeignKey(Registratsiya, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=False)
    keywords = models.TextField()
    # image=models.ImageField(upload_to='image/',blank=False)


    def __str__(self):
        return self.title
