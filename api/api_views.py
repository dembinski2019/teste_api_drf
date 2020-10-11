from rest_framework import viewsets
from .serializers import CategorySerializer, ProductSerializer
from .models import Category, Product


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class =  ProductSerializer
    queryset = Product.objects.all()




