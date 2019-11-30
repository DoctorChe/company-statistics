from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand
from authapp.models import User


class Command(BaseCommand):
    help = 'Fill DB new data'

    def handle(self, *args, **options):

        if not User.objects.filter(username='admin'):
            print('Create new superuser')
            User.objects.create_superuser('admin', 'admin@companystatictics.local', 'admin')

        if not User.objects.filter(username='user'):
            print('Create new company user')
            User.objects.create_user('user', password='user')

        if not User.objects.filter(username='editor'):
            print('Create new company editor')
            User.objects.create_user('editor', password='editor')

        # # Add group 'Editor'
        # group = Group(name='Editor')
        # group.save()
        # user = User.objects.filter(username='editor')
        # user.groups.addgroup(group)
