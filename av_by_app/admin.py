from django.contrib import admin

from django.contrib import admin
from .models import Ad

# Зарегистрируем модель Advertisement для административной панели
@admin.register(Ad)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'created_at')  # Поля, отображаемые в списке объектов
    search_fields = ('title', 'description')         # Поля, по которым можно осуществлять поиск
    list_filter = ('created_at',)                # Поля, по которым можно фильтровать



# Register your models here.
