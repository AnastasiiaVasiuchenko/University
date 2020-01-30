import random
from django.core.management.base import BaseCommand, CommandError
from students.models import Student, Group


class Command(BaseCommand):
    help = 'Generate 100 random students'

    def add_arguments(self, parser):
        parser.add_argument(
            '--number',
            help='Enter number of students'
        )

    def handle(self, *args, **options):
        groups = [Group.generate_group() for i in range(10)]
        number = int(options.get('number') or 100)

        for i in range(number):
            student = Student.generate_student()
            student.group_id = random.choice(groups)
            student.save()
