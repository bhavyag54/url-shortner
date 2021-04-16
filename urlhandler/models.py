from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class shorturl(models.Model):
    original_url = models.CharField(blank=False, max_length=1000)
    short_url = models.CharField(blank=False, max_length=8)
    visits = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user} : {self.original_url[:20]}"
