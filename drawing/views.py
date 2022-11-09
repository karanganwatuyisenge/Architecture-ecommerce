from django.shortcuts import render
from .models import Category

# Create your views here.
# Home age
def home(request):
    data=Category.objects
    return render(request,'index.html')

#category
def category_list(request):
    return render(request,'category_list.html')
#Brand