from django.conf import settings
from django.contrib import admin
from rest_framework import routers
from django.urls import path, include
from django.conf.urls.static import static

from Products.api_views import *


router = routers.DefaultRouter()
router.register('Product', ProductViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Applications
    path('', include('main.urls')),
    path('profile/', include('Profile.urls')),
    path('product/', include('Products.urls')),

    # DRF
    path('api/', include(router.urls)),
    path('api-rest/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
urlpatterns += static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT
)
