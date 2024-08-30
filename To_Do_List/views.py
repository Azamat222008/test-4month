from django.shortcuts import render
from .models import Task, Category
from django.db.models import Q
from django import forms
from django.views import View
from django.urls import reverse
from django.shortcuts import get_object_or_404


def task_list(request):
    category_filter = request.GET.get('category')
    search_query = request.GET.get('search', '')

    tasks = Task.objects.all()

    if category_filter:
        tasks = tasks.filter(category__id=category_filter)
    if search_query:
        tasks = tasks.filter(Q(title__icontains=search_query))

    categories = Category.objects.all()

    return render(request, 'task_list.html', {'tasks': tasks, 'categories': categories})



class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'category']

class TaskCreateView(View):
    def get(self, request):
        form = TaskForm()
        return render(request, 'task_create.html', {'form': form})

    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return render(reverse('task_list'))
        return render(request, 'task_create.html', {'form': form})


def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'detail_task.html', {'task': task})