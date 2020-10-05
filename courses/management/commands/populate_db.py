from django.core.management.base import BaseCommand
from mixer.backend.django import mixer

from courses.models import Course


class Command(BaseCommand):

    help = 'Generate Courses Data'

    def handle(self, *args, **options):
        
        course = mixer.blend(Course)
        print(course)
