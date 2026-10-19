from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from .models import CloudFile
from .serializers import CloudFileSerializer

class CloudFileViewSet(viewsets.ModelViewSet):
    queryset = CloudFile.objects.all().order_by('-uploaded_at')
    serializer_class = CloudFileSerializer
    parser_classes = (MultiPartParser, FormParser) # Crucial para recibir archivos