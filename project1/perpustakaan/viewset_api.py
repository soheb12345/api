from perpustakaan.models import Kelompok
from perpustakaan.serializers import KelompokSerializers
from rest_framework import viewsets

class KelompokViewset(viewsets.ModelViewSet):
    queryset = Kelompok.objects.all()
    serializer_class = KelompokSerializers