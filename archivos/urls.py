from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CloudFileViewSet

router = DefaultRouter()
router.register(r'files', CloudFileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]