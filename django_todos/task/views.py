from django.shortcuts import render
from django.http import HttpResponse
from task.models import Task
# Create your views here.


def home(request):
    c={
        'name': 'Gali'
    }
    return render(request, 'task/home.html', c)


def task_delete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return HttpResponse('shanchuchenggong')


def task_create(request):
    content=request.POST.get('task')
    task = Task(content=content)
    task.save()
    return HttpResponse('ok')


def task_list(request):
    tasks = Task.objects.all()
    c={
        'todos': tasks
    }
    for task in tasks:
        print(task.content)
    return render(request, 'task/list.html', c)
