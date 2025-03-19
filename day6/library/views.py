
from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from library.models import Author,Genre,Book
from django.http import JsonResponse

import json
# Create your views here.
@csrf_exempt
def book_view(request, name="JK rolin", title="Harry Potter"):
  """
  api: library/
  
  method: post,get,put,delete
  operations: used to retrive, create, update and delte books from library
  
  1) post:
     used to create author, book and genre tables
     author has one to many relation with book
     book has many to many relation with genre
     
  2)Get: 
  used to retrive books of specific author
  used to retrive authors of specific genre
  
  3)Put:
  used to update the price of specific book
  
  
  4) delete:
  used to delete genre from specific book
  
  """
  if request.method == "POST":
    data = json.loads(request.body)
    author = Author.objects.create(
      name = data['author'],
      birthdate = data['birthdate'],
      nationality = data['nationality']
    )
    author.save()
    genre= Genre.objects.create(genre=data['genre'])
    genre.save()
    book = Book.objects.create(
      title = data['title'],
      author= author,
      publication_date = data['publication_date'],
      price = data['price'],
    )
    book.save()
    book.genre.add(genre)

    remodel_book = model_to_dict(book)
    remodel_book["genre"] = list(book.genre.values("id", "genre"))
    
    return JsonResponse(remodel_book, safe=False)
 
  elif request.method == "GET":
    specific_author = list(Book.objects.filter(author__name = name).values())
    
    specific_genre = list(Book.objects.filter(genre__genre= "fiction").values("author__name"))
    
    return JsonResponse({"specific_author": specific_author, "specific_genre": specific_genre}, safe=False)
  
  elif request.method == "PUT":
    book = get_object_or_404(Book, title= title)
    book.price = 700.43
    book.save()
    remodel_book = model_to_dict(book)
    remodel_book["genre"] = list(book.genre.values())
    return JsonResponse(remodel_book,status=200)
  elif request.method == "DELETE":
    book = get_object_or_404(Book, title=title)
    book.genre.clear()
    book.save()
    remodel_book = model_to_dict(book)
    return JsonResponse(remodel_book, status=200)