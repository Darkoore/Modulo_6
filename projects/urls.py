from django.urls import path
from .views import DashboardView, ProjectCreateView, ProjectUpdateView, ProjectDeleteView, TaskCreateView

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('create/', ProjectCreateView.as_view(), name='create_project'),
    path('edit/<int:pk>/', ProjectUpdateView.as_view(), name='edit_project'),
    path('delete/<int:pk>/', ProjectDeleteView.as_view(), name='delete_project'),
    path('task/create/<int:pk>/', TaskCreateView.as_view(), name='create_task'),
]