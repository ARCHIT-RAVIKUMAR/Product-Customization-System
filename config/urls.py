from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse, HttpResponse
import os

def home(request):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    index_path = os.path.join(base_dir, 'index.html')
    with open(index_path, 'r') as f:
        return HttpResponse(f.read(), content_type='text/html')

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
]