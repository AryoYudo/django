from django.contrib import admin
from django.urls import path, include  # Import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('nama_aplikasi.urls')),  # Sertakan URL dari aplikasi
]
