from django.shortcuts import render, redirect
from django.http import HttpResponse
# Use datetime if not localizing timezones
import datetime
# Otherwise use timezone
from django.utils import timezone
from .models import *
from .forms import *
from django.utils.timezone import make_aware

# Create your views here.


def index(request):

    # tasks = Tasks.objects.all()
    tasks = Tasks.objects.order_by('due_date')
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks': tasks, 'form': form}
    context['count'] = context['tasks'].filter(complete=False).count()
    search_input = request.GET.get('search-area') or ''
    if search_input:
        context['tasks'] = context['tasks'].filter(
            title__startswith=search_input)

        context['search_input'] = search_input

    return render(request, 'todo/list.html', context)


def updateTask(request, pk):
    task = Tasks.objects.get(id=pk)

    form = UpdateForm(instance=task)

    if request.method == 'POST':
        form = UpdateForm(request.POST, instance=task)
        if form.is_valid():
            # test = make_aware(form.cleaned_data["due_date"])
            # print(test)
            form.save()
            return redirect('/')
    # print(form)
    context = {'form': form, 'task': task, 'name': "Update Task"}

    return render(request, 'todo/update_task.html', context)


def createTask(request):

    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form, "name": "Add Task"}

    return render(request, 'todo/update_task.html', context)


def deleteTask(request, pk):
    task = Tasks.objects.get(id=pk)

    if request.method == 'POST':
        task.delete()
        return redirect('/')

    context = {'task': task}
    return render(request, 'todo/delete_task.html', context)
