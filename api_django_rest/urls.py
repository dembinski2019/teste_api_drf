from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views
from api.api_views import CategoryViewSet, ProductViewSet



router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)




urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls+[path('auth',views.obtain_auth_token)])),
    path('api-auth/',include('rest_framework.urls', namespace='rest_framework')),
]
