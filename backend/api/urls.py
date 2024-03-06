from rest_framework.routers import DefaultRouter
from safemed.api.urls import router_rest
from django.urls import path, include


router = DefaultRouter()

router.registry.extend(router_rest.registry)

urlpatterns = [
    path('', include(router.urls))
]