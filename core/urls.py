from django.urls import re_path, include
from rest_framework import routers

from core.viewsets import CountryViewSet, CityViewSet, PositionViewSet, AreaViewSet, IndustryViewSet, CategoryRoleViewSet

router = routers.DefaultRouter()
router.register(r'country', CountryViewSet)
router.register(r'city', CityViewSet)
router.register(r'position', PositionViewSet)
router.register(r'area', AreaViewSet)
router.register(r'industry', IndustryViewSet)
router.register(r'category-role', CategoryRoleViewSet)


urlpatterns = [
    re_path(r'^', include(router.urls)),
]
