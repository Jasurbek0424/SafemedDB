from rest_framework import serializers
from ..models import MainCategory, Category, SubCategory, Brand, Product, Contacts

class MainCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MainCategory
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SubCategorySerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    class Meta:
        model = SubCategory
        fields = '__all__'

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    sub_category = serializers.StringRelatedField()
    brand = serializers.StringRelatedField(source='brand.name')
    image = serializers.StringRelatedField(source='image.name')
    class Meta:
        model = Product
        # image = serializers.Field('image.url')
        fields = ('id', 'title', 'description', 'category', 'sub_category', 'brand', 'image_url', 'image')
        #'get_image'

class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'