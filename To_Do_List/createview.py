from django.shortcuts import render
from .models import Task, Category
from django.db.models import Q
from django import forms
from django.views import View
from django.urls import reverse

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
            return redirect(reverse('task_list'))
        return render(request, 'task_create.html', {'form': form})