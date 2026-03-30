from django.test import TestCase
from django.contrib.auth.models import User
from .models import Project
from django.urls import reverse

class ProjectTest(TestCase):

    def test_create_project(self):
        user = User.objects.create(username='test')

        project = Project.objects.create(
            name='Proyecto Test',
            description='Descripción',
            owner=user
        )

        self.assertEqual(project.name, 'Proyecto Test')




class ViewTest(TestCase):

    def test_dashboard_requires_login(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)  # redirige a login


class AuthTest(TestCase):

    def test_logged_user_access(self):
        user = User.objects.create_user(username='test', password='1234')
        self.client.login(username='test', password='1234')

        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)