from rest_framework.views import APIView
from rest_framework.response import Response
from products.models import Product

class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.filter(is_active=True)
        data = [{'id': str(p.id), 'name': p.name, 'category': p.category} for p in products]
        return Response(data)