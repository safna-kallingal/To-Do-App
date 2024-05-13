from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.shortcuts import render
from .utils.github_utils import save_gist_locally

def index(request):
    tasks = Task.objects.all()
    total_tasks = tasks.count()
    completed_tasks = tasks.filter(complete=True).count()  # Filter for completed tasks

    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {
        'tasks': tasks,
        'form': form,
        'completed_tasks': completed_tasks,
        'total_tasks': total_tasks,
    }
    return render(request, 'tasks/list.html', context)

def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'tasks/update_task.html', context)

def deleteTask(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == "POST":
        item.delete()
        return redirect('/')

    context = {'item': item}
    return render (request, 'tasks/delete.html',context) 
# views.py



def save_gist_to_local(request,pk):
    # Example gist ID and file path
    Task.objects.get(id=pk)
    gist_id = "https://gist.github.com/safna-kallingal/a328e1fb3e33c7bcf1380bedf6b88048"  # Replace with actual gist ID
    file_path = "todo.md"     # Specify desired file path
    
    # Call utility function to save gist locally
    success, message = save_gist_locally(gist_id, file_path)
    
    if success:
        return render(request, "success_gist.html", {"Successful": message})
    else:
        return render(request, "error_gist.html", {"Unseccessful": message})
