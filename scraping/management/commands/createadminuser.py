from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Create a new admin user'

    def handle(self, *args, **kwargs):
        User.objects.create_superuser(username='admin', email='admin@example.com', password="password",
                                      first_name='Admin', last_name='Example')
        self.stdout.write('Created a new admin user')
