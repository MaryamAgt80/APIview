from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime


class Book(models.Model):
    name = models.CharField(max_length=100)
    store_name = models.CharField(max_length=100)
    fav = models.BooleanField(default=False)
    description = models.TextField()
    image = models.ImageField(upload_to='image', default='')
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural='کتاب ها'
        verbose_name='کتاب'

