from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):

    help = 'Create SuperUser'

    def handle(self, *args, **options):
        
        user = 'admin'
        password = 'password'
        email = 'email@test.com'
        User.objects.create_superuser(user, email, password)
