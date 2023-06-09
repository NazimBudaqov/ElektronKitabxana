from django.contrib import admin
from django.urls import path, include

# http://127.0.0.1:8000/ ==> ana sehifeye gedir #1
# http://127.0.0.1:8000/index ==> ana sehifeye gedir #2
# http://127.0.0.1:8000/books ==> books sayfasina
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('',include('ElektronKitabxana.urls')),
    path('istifadeci/',include('istifadeci.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
