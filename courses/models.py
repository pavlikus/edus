from django.db import models
from django.urls import reverse, reverse_lazy

from sorl.thumbnail import ImageField
from sorl.thumbnail import get_thumbnail

from members.models import Student, Teacher


class Course(models.Model):

    name = models.CharField(max_length=64)
    description = models.TextField()
    logo = ImageField(default='images/courses/placeholder.png',
                      upload_to='images/courses/')
    teachers = models.ManyToManyField(Teacher,
                                      related_name='courses')
    slug = models.SlugField()

    def get_absolute_url(self):
        return reverse('course', args=[self.slug])

    def get_edit_url(self):
        return reverse('course_edit', args=[self.slug])

    def get_delete_url(self):
        return reverse('course_delete', args=[self.slug])

    def __str__(self):
        return self.name


class CourseStream(models.Model):

    name = models.CharField(max_length=64)
    courses = models.ForeignKey(Course,
                                related_name='course_streams',
                                on_delete=models.CASCADE)
    students = models.ManyToManyField(Student,
                                      related_name='course_streams')
    date_start = models.DateField()
    date_end = models.DateField()

    def __str__(self):
        return self.name


class Schedule(models.Model):

    title = models.CharField(max_length=64)
    description= models.TextField()
    teacher = models.ForeignKey(Teacher,
                                related_name='schedulers',
                                on_delete=models.CASCADE)
    course_stream = models.ForeignKey(CourseStream,
                                      related_name='schedulers',
                                      on_delete=models.CASCADE)
    time_start = models.DateTimeField()
