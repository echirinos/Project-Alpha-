from django.shortcuts import render
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView
from tasks.models import Task
from django.contrib.auth.mixins import LoginRequiredMixin


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "tasks/create.html"
    fields = [
        "name",
        "start_date",
        "due_date",
        "project",
        "assignee",
    ]

    def get_success_url(self):
        return reverse("show_project", kwargs={"pk": self.object.project.pk})


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "tasks/mine.html"

    def get_queryset(self):
        return Task.objects.filter(assignee=self.request.user)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = "tasks/update.html"
    fields = ["is_completed"]
    success_url = reverse_lazy("show_my_tasks")
