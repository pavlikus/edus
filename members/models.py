from django.db import models
from django.urls import reverse

from sorl.thumbnail import ImageField
from sorl.thumbnail import get_thumbnail


class Member(models.Model):

    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    bio = models.TextField()

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
        
    def __str__(self):
        return self.full_name

    class Meta:

        abstract = True


class Teacher(Member):

    
    avatar = ImageField(default='images/members/avatar.png',
                       upload_to='images/members/teachers/')
    position = models.CharField(max_length=64)
    slug = models.SlugField(unique=True)

    @property
    def title(self):
        return f"{self.full_name} - {self.position}"

    def get_absolute_url(self):
        return reverse('teachers:teacher', args=[self.slug])


class Student(Member):

    avatar = ImageField(default='images/members/avatar.png',
                        upload_to='images/members/students/')
