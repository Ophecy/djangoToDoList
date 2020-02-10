from django.shortcuts import render, redirect
from .models import TodoList
from .forms import TodoForm

from django.views.decorators.http import require_POST
# Create your views here.


def index(request):
    todo_list = TodoList.objects.order_by('id')
    form = TodoForm()
    context = {'todo_list': todo_list, "form": form}
    return render(request, "todolist/index.html", context)


@require_POST
def addTodo(request):
    form = TodoForm(request.POST)

    if form.is_valid():
        new_todo = TodoList(text= request.POST['text'])
        new_todo.save()

    return redirect('index')

