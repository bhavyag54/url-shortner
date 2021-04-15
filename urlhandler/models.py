from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class shorturl(models.Model):
    original_url = models.URLField(blank = False)
    short_url = models.CharField(blank=False, max_length=8)
    visits = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    