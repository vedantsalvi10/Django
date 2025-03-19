from django.db import models

# Create your models here.
class Author(models.Model):
  name = models.CharField(max_length=50)
  birthdate = models.DateField()
  nationality = models.CharField(max_length=50)
class Genre(models.Model):
  genre = models.CharField(max_length=255)
  
class Book(models.Model):
  title = models.CharField(max_length=50)
  author = models.ForeignKey(Author, on_delete= models.CASCADE)
  genre = models.ManyToManyField(Genre)
  publication_date = models.DateField()
  price = models.DecimalField(max_digits=8, decimal_places=2)



  