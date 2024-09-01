from rest_framework import serializers
from .models import PassportPhoto
from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'full_name', 'inn', 'is_verified']


class PassportPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PassportPhoto
        fields = ['passport_page_1', 'passport_page_2', 'selfie_with_passport', 'expiration_date']
