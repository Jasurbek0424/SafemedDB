from import_export import resources, fields
from .models import Product, Brand, Category, SubCategory


class ImageURLField(fields.Field):
    def clean(self, value, row=None, *args, **kwargs):
        if value is None or value.strip() == "":
            return "https://m.media-amazon.com/images/I/21cOE-lrhBL._AC_UF1000,1000_QL80_.jpg"  # Значение по умолчанию
        else:
            return value.strip()

class ProductResource(resources.ModelResource):
    image_url = ImageURLField(attribute='image')
    category = fields.Field(column_name='category', attribute='category__title')
    subcategory = fields.Field(column_name='subcategory', attribute='sub_category__title')
    brand = fields.Field(column_name='brand', attribute='brand__name')

    class Meta:
        model = Product
        fields = ('id','title', 'image_url', 'category', 'subcategory', 'description', 'brand')

    def before_import_row(self, row, **kwargs):
        try:
            category_title = row['category']
            category_obj = Category.objects.get(title=category_title)
            row['category'] = category_obj
        except Category.DoesNotExist:
            pass

        try:
            subcategory_title = row.get('subcategory')
            if subcategory_title:
                subcategory_obj = SubCategory.objects.get(title=subcategory_title)
                row['subcategory'] = subcategory_obj
        except SubCategory.DoesNotExist:
            pass

        try:
            brand_name = row.get('brand')
            if brand_name:
                brand_obj = Brand.objects.get(name=brand_name)
                row['brand'] = brand_obj
        except Brand.DoesNotExist:
            pass


class BrandResource(resources.ModelResource):
    class Meta:
        model = Brand

class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category

class SubCategoryResource(resources.ModelResource):
    category = fields.Field(column_name='category', attribute='get_category_display')

    def before_import_row(self, row, **kwargs):
        category_title = row['category']
        category_obj = Category.objects.filter(title=category_title).first()
        if category_obj:
            row['category'] = category_obj.id
        else:
            pass

    class Meta:
        model = SubCategory
        fields = ('id', 'category', 'title')