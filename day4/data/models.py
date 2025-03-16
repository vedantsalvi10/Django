from django.db import models

# Create your models here.

class Profile(models.Model):
  name = models.CharField(max_length=255)
  email = models.EmailField(unique=True)
  mobile_number = models.CharField(max_length=11)
  address = models.TextField(default=None)
  
  def __str__(self):
    return self.name