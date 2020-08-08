
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

from productos.views import JugoViewSet

router = DefaultRouter()
router.register(r'productos', JugoViewSet)

urlpatterns = router.urls

urlpatterns += [
    path('admin/', admin.site.urls),
]
