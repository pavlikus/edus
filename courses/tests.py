from django.contrib.auth.models import User
from django.forms.models import model_to_dict
from django.test import TestCase
from django.test.client import Client
from django.urls import reverse

from mixer.backend.django import mixer

import pytest

from .models import Course, CourseStream


@pytest.mark.django_db
@pytest.fixture(autouse=True, scope='class')
def superuser_create_and_login(request):

    password = 'password'
    admin = User.objects.create_superuser('user',
                                          'email@test.com',
                                          password)
    client = Client()
    client.login(username=admin.username, password=password)
    request.cls.admin_client = client


@pytest.mark.django_db
class CourseTest(TestCase):
    
    fixtures = ['courses.json', 'members.json']
    
    def test_course_model_add(self):
        
        count = Course.objects.count()
        course = mixer.blend(Course)
        assert count != Course.objects.count()
        
    def test_coursestream_model_add(self):
        
        course = Course.objects.last()
        course_stream_count = CourseStream.objects.filter(courses=course).count()
        course_stream_all_count = CourseStream.objects.count()
        course_stream = mixer.cycle(10).blend(CourseStream, courses=course)
        assert course_stream_all_count != CourseStream.objects.count()
        assert course_stream_count != CourseStream.objects.filter(courses=course).count()
    
    def test_course_create_response_redirect(self):

        response = self.client.get(reverse('course_add'))
        assert response.status_code == 302
        
    def test_course_create_response_ok(self):

        response = self.admin_client.get(reverse('course_add'))
        assert response.status_code == 200
        
    def test_course_create_view(self):
        
        course = mixer.blend(Course)
        response = self.client.post(reverse('course_add'), model_to_dict(course))
        assert course == Course.objects.last()

    def test_course_delete_view_login_required(self):
        
        course = Course.objects.last()
        response = self.client.post(reverse('course_delete', args=[course.slug]), follow=True)
        assert response.status_code == 200
        assert course == Course.objects.last()
        
    def test_course_delete_view(self):
        
        course = Course.objects.last()
        response = self.admin_client.post(reverse('course_delete', args=[course.slug]), follow=True)
        assert response.status_code == 200
        assert course != Course.objects.last()
        
    def test_course_edit_view(self):
        
        course = Course.objects.last()
        course.description = "<p></p>"
        response = self.admin_client.post(reverse('course_edit', args=[course.slug]), model_to_dict(course), follow=True)
        assert response.status_code == 200
        assert course.description == Course.objects.last().description
