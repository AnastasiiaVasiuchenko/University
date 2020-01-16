from django.core.management.base import BaseCommand, CommandError
from students.models import Group


class Command(BaseCommand):
    help = 'Generate 100 random groups'

    def handle(self, *args, **options):
        for i in range(100):
            Group.generate_group()