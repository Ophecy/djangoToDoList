from django.shortcuts import render
from .models import TodoList
from .forms import TodoForm
# Create your views here.


def index(request):
    todo_list = TodoList.objects.order_by('id')
    form = TodoForm()
    context = {'todo_list': todo_list, "form": form}
    return render(request, "todolist/index.html", context)
