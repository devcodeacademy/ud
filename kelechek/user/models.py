from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=255)
    inn = models.CharField(max_length=20)
    is_verified = models.BooleanField(default=False)


class PassportPhoto(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='passport_photo')
    passport_page_1 = models.ImageField(upload_to='passport_photos/')
    passport_page_2 = models.ImageField(upload_to='passport_photos/')
    selfie_with_passport = models.ImageField(upload_to='selfie_photos/')
    expiration_date = models.DateField()
