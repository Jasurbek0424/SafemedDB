from django.contrib import admin
from django.conf import settings
from import_export import fields, resources
from import_export.admin import ImportExportModelAdmin
from .models import Category, SubCategory, Brand, Product, Contacts

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Brand)
admin.site.register(Contacts)


class ProductResource(resources.ModelResource):
    import_id = fields.Field(column_name='import_id', attribute='import_id')

    class Meta:
        model = Product
        fields = ('import_id', 'title', 'image', 'category', 'subcategory', 'description', 'brand')

    def before_import_row(self, row, **kwargs):
        try:
            del row['id']
        except KeyError:
            pass  # Пропускаем, если столбец 'id' отсутствует

    def after_import_instance(self, instance, new, **kwargs):
        # После импорта удалите временный столбец 'import_id'
        if hasattr(instance, 'import_id'):
            delattr(instance, 'import_id')
        instance.save()

class ProductAdmin(ImportExportModelAdmin):
    list_display = ('title', 'category', 'sub_category', 'brand', 'description', 'image')
    search_fields = ('title', 'category__title', 'sub_category__title', 'brand__name')
    list_filter = ('category', 'sub_category', 'brand')
    resource_class = ProductResource

admin.site.register(Product, ProductAdmin)