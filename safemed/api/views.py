from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from ..models import Category, SubCategory, Brand, Product, Contacts, MainCategory
from .serializers import CategorySerializer, SubCategorySerializer, BrandSerializer, ProductSerializer, ContactsSerializer, MainCategorySerializer





class MainCategoryViewSet(ModelViewSet):
    queryset = MainCategory.objects.all()
    serializer_class = MainCategorySerializer
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SubCategoryViewSet(ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer

class BrandViewSet(ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ContactsViewSet(ModelViewSet):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer