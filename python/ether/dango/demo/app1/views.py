from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
# Create your views here.



def index1(request):
  return HttpResponse("Hi Praveen")

def index(request):
  data = Question.objects.all()
  return render(request,'index.html',{"data":data})
