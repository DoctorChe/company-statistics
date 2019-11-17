from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Fill DB new data'

    def handle(self, *args, **options):

        # Создаём суперпользователя при помощи менеджера модели
        if not User.objects.filter(username='admin'):
            print('Create new superuser')
            User.objects.create_superuser('admin', 'admin@companystatictics.local', 'admin')
