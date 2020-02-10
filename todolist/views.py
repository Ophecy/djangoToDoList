from django.shortcuts import render
from .models import TodoList

# Create your views here.


def index(request):
    todo_list = TodoList.objects.order_by('id')
    context = {'todo_list': todo_list}
    return render(request, "todolist/index.html", context)
