from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.

def index(request):
    tasks = Task.objects.all()[0:6]
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'index.html', {'tasks': tasks, 'form': form})

def update(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'update.html', {'task': task, 'form': form})

def deleted(request, pk):
    item = Task.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    return render(request, 'deleted.html', {'item': item})
