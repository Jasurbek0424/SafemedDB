from .views import CategoryViewSet, SubCategoryViewSet, BrandViewSet, ProductViewSet, ContactsViewSet
from rest_framework.routers import DefaultRouter


router_rest = DefaultRouter()
router_rest.register(r'categories', CategoryViewSet)
router_rest.register(r'subcategories', SubCategoryViewSet)
router_rest.register(r'brands', BrandViewSet)
router_rest.register(r'products', ProductViewSet)
router_rest.register(r'contacts', ContactsViewSet)