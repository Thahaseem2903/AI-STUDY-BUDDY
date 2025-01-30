
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .models import File
from .serializers import FileSerializer
from rest_framework import status
import PyPDF2

class FileUploadView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save(user=request.user)
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetJWTTokenView(APIView):
    def post(self, request):
        pass
    