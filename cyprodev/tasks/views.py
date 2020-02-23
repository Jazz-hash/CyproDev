from django.shortcuts import render
from .models import Task
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from cyprodev.mixins import FormUserNeededMixin, UserOwnerMixin
from .forms import TaskModelForm
# Create your views here.


class TasksListView(LoginRequiredMixin, ListView):
    model = Task

    def get_context_data(self, **kwargs):
        context = super(TasksListView, self).get_context_data(**kwargs)
        context['head'] = 'Tasks'
        context['sub_head'] = 'List'
        return context

    def get_queryset(self):
        queryset = super(TasksListView, self).get_queryset()
        if self.request.user.is_superuser:
            queryset = Task.objects.all()
        else:
            queryset = Task.objects.filter(user=self.request.user)
        return queryset


class TasksDetailView(LoginRequiredMixin, DetailView):
    model = Task

    def get_context_data(self, **kwargs):
        context = super(TasksDetailView, self).get_context_data(**kwargs)
        context['head'] = 'Tasks'
        context['sub_head'] = 'Details'
        return context


class TasksDeleteView(LoginRequiredMixin, DeleteView):
    model = Task

    def get_context_data(self, **kwargs):
        context = super(TasksDeleteView, self).get_context_data(**kwargs)
        context['head'] = 'Tasks'
        context['sub_head'] = 'Remove'
        return context


class TasksCreateView(FormUserNeededMixin, LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskModelForm
    template_name = 'tasks/task_add.html'

    def get_context_data(self, **kwargs):
        context = super(TasksCreateView, self).get_context_data(**kwargs)
        context['head'] = 'Tasks'
        context['sub_head'] = 'New'
        return context


class TasksUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
    model = Task
    form_class = TaskModelForm
    template_name = 'tasks/task_edit.html'

    def get_context_data(self, **kwargs):
        context = super(TasksUpdateView, self).get_context_data(**kwargs)
        context['head'] = 'Tasks'
        context['sub_head'] = 'Edit'
        return context
