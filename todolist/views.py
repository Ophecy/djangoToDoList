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
        new_todo = TodoList(text=request.POST['text'])
        new_todo.save()

    return redirect('index')


def completeTodo(request, todo_id):
    todolist = TodoList.objects.get(pk=todo_id)
    todolist.complete = True
    todolist.save()
    return redirect('index')


def deleteTodo(request):
    todolist = TodoList.objects.filter(complete__exact=True).delete()
    return redirect('index')
