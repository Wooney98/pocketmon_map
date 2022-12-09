from django.db import models

# Create your models here.
class Pocket(models.Model):
    img_url = models.URLField()
    name = models.TextField(max_length=10)
    link = models.CharField(max_length=200)
    height = models.CharField(max_length=10)
    weight = models.CharField(max_length=10)
    classify = models.TextField(max_length=10)
    character = models.TextField(max_length=50) # 긴글
    
    class Meta:
        verbose_name_plural = "포켓몬"
        ordering = ('name',)
    def __str__(self):
        return f"{self.name} -- {self.height} -- {self.weight} -- {self.classify} -- {self.character}"
    