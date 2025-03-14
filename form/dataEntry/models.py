from django.db import models
# Create your models here.
class Profile(models.Model):
  departments = [
    ("bca" , "BCA"),
    ("ba" , "BA"),
    ("bcom", "BCOM"),
    ('bba', "BBA"),
  ]
  name = models.CharField(max_length=255)
  address = models.TextField()
  contact = models.IntegerField()
  department = models.CharField(max_length=20,choices=departments)
  email = models.EmailField(max_length=50, null=True)