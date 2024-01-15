# Модуль данных для объявлений

from django.db import models
from django.contrib.auth.models import User

class Ad(models.Model):
    CATEGORY_CHOICES = [
        ('auto', 'Автомобили'),
        ('real_estate', 'Недвижимость'),
        # Другие категории
    ]
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField()
    image = models.ImageField(upload_to='ad_images', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)



# Create your models here.
