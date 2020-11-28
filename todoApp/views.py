from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib import messages

# Create your views here.
def index(request):
    title = 'HELLO FROM HXKOEY'

    # SHOW FORM
    form = TaskCreateForm
    if request.method == 'POST':
        form = TaskCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Saved successfully')
            return redirect('/')

    # SHOW DATABASE
    queryset = Task.objects.all()

    context = {'title': title, 'form': form, 'queryset': queryset}
    return render(request, 'todoApp/index.html', context)

def update(request, pk):
    queryset = Task.objects.get(id=pk)
    form = TaskUpdateForm(instance=queryset)

    if request.method == 'POST':
        form = TaskUpdateForm(request.POST, instance=queryset)
        form.save()
        messages.success(request,'Updated successfully')
        return redirect('/')


    context = {'form': form}
    return render(request, 'todoApp/update.html', context)

def delete(request, pk):
    queryset = Task.objects.get(id=pk)

    if request.method == 'POST':
        queryset.delete()
        messages.success(request,'Deleted successfully')
        return redirect('/')

    context = {'queryset': queryset}
    return render(request, 'todoApp/delete.html', context)
