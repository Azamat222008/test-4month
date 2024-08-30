from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .models import Task, Category
from django.db.models import Q

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'detail_task.html', {'task': task})