from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def home(request):
    return JsonResponse({
        'message': 'Product Customization System is running!',
        'endpoints': {
            'products': '/api/v1/products/',
            'admin': '/admin/',
        }
    })

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
]