from django.shortcuts import render, redirect
from .models import TodoItem,Dnditem
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'home.html')

def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items })

def itemList(request):
    items = Dnditem.objects.all()
    return render(request, "itemList.html", {"defaultItems": items })

def run_script(request):
    if request.method == "POST":
        print ("Button CLICKED")
        return redirect('run_script') 
    return HttpResponse('Invalid Request')