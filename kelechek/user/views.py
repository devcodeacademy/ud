from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.contrib.auth import login
from .serializers import UserSerializer, PassportPhotoSerializer
from .models import CustomUser, PassportPhoto
from .utils import verify_user


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        user = serializer.save()
        passport_data = self.request.data.get('passport_photo')

        if passport_data:
            passport_serializer = PassportPhotoSerializer(data=passport_data)
            if passport_serializer.is_valid():
                passport_photo = passport_serializer.save(user=user)

                # Verifying the user's passport information
                verified, message = verify_user(user)

                if verified:
                    # Auto-logining the user after successful verification
                    login(self.request, user)
                else:
                    # Handle case where passport is expired or verification failed
                    user.delete()  # Delete the user if verification fails
                    return Response({"error": message}, status=status.HTTP_400_BAD_REQUEST)
            else:
                # Handle invalid passport data
                user.delete()  # Delete the user if passport data is invalid
                return Response(passport_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            # Handle case where passport data is not provided
            user.delete()  # Delete the user if no passport data is provided
            return Response({"error": "Passport data is required."}, status=status.HTTP_400_BAD_REQUEST)
