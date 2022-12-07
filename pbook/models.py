from django.db import models

# Create your models here.
class Pocket(models.Model):
    img_url = models.URLField()
    name = models.TextField(max_length=10)
    type = models.TextField(max_length=10)
    height = models.CharField(max_length=10)
    weight = models.CharField(max_length=10)
    classify = models.TextField(max_length=10)
    character = models.TextField(max_length=50) # 긴글
    detail = models.TextField(max_length=50) # 물음표