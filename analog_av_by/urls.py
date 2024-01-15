from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from av_by_app.views import AdViewSet
# from av_by_app import views

router = DefaultRouter()
router.register(r'ads', AdViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),

]


# Создаем router и регистрируем представления API
# router = DefaultRouter()
# router.register(r'api/ad', AdvertisementViewSet)
