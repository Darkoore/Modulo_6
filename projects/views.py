from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Project, Task

class DashboardView(LoginRequiredMixin, ListView):
    model = Project
    template_name = 'projects/dashboard.html'

    def get_queryset(self):
        return Project.objects.filter(owner=self.request.user)


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    fields = ['name', 'description']
    template_name = 'projects/project_form.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    fields = ['name', 'description']
    template_name = 'projects/project_form.html'
    success_url = '/'

class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    template_name = 'projects/project_confirm_delete.html'
    success_url = reverse_lazy('dashboard')

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'completed']
    template_name = 'projects/task_form.html'

    def form_valid(self, form):
        form.instance.project_id = self.kwargs['pk']
        form.instance.assigned_to = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return '/'