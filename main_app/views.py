from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

class Finch:
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

finches = [
  Finch('Carl', 'Tropical Borneo', 'Likes Halloween', 3),
  Finch('Peggy', 'Finch', 'Likes Art', 0),
  Finch('Freddy', 'Finch', 'Happy fluff ball.', 4),
  Finch('Susan', 'Zebra Finch', 'Likes to People Watch', 6)
]

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello Birdies!</h1>')

def about(request):
  return render(request, 'about.html')

def finches_index(request):
  return render(request, 'finches/index.html', { 'finches': finches })