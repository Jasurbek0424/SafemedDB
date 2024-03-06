from django.contrib import admin
from .resource import ProductResource, BrandResource, CategoryResource, SubCategoryResource
from import_export.admin import ImportExportModelAdmin
from .models import Category, SubCategory, Brand, Product, Contacts



class ProductAdmin(ImportExportModelAdmin):
    list_display = ('id', 'title', 'category', 'sub_category', 'brand', 'description', 'image')
    search_fields = ('id', 'title', 'category__title', 'sub_category__title', 'brand__name')
    list_filter = ('category', 'sub_category', 'brand')
    resource_class = ProductResource

class BrandAdmin(ImportExportModelAdmin):
    resource_class = BrandResource

class CategoryAdmin(ImportExportModelAdmin):
    resource_class = CategoryResource

class SubCategoryAdmin(ImportExportModelAdmin):
    resource_class = SubCategoryResource
    
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Contacts)
