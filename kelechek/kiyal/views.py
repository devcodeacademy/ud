from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Premises
from .serializers import PremisesSerializer

class PremisesList(APIView):
    def get(self, request):
        premises = Premises.objects.all()
        serializer = PremisesSerializer(premises, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = PremisesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PremisesDetail(APIView):
    def get(self, request, pk):
        try:
            premises = Premises.objects.get(pk=pk)
        except Premises.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = PremisesSerializer(premises, context={'request': request})
        return Response(serializer.data)
