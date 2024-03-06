from import_export import resources, fields
from .models import Product, Brand, Category, SubCategory

class ProductResource(resources.ModelResource):
    category = fields.Field(column_name='category', attribute='category__title')
    subcategory = fields.Field(column_name='subcategory', attribute='sub_category__title')
    brand = fields.Field(column_name='brand', attribute='brand__name')

    class Meta:
        model = Product
        fields = ('id','title', 'image', 'category', 'subcategory', 'description', 'brand')

class BrandResource(resources.ModelResource):
    class Meta:
        model = Brand

class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category

class SubCategoryResource(resources.ModelResource):
    class Meta:
        model = SubCategory