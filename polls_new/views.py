from django.shortcuts import render
from .models import Bio

# Create your views here.


def index(request):
  return render(request,'polls_new/index.html')