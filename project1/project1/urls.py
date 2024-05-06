from django.contrib import admin
from django.urls import path, include
from perpustakaan.views import buku, penerbit
from perpustakaan.viewset_api import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('kelompok', KelompokViewset)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('buku/', buku),
     path('penerbit/', penerbit),
]
