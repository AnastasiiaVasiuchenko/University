import random
from django.core.management.base import BaseCommand, CommandError
from students.models import Group, Student
from teachers.models import Teacher


class Command(BaseCommand):
    help = 'Generate 100 random groups'

    def add_arguments(self, parser):
        parser.add_argument(
            '--number',
            help='Enter number of groups'
        )

    def handle(self, *args, **options):
        number = int(options.get('number') or 100)
        students = [Student.generate_student() for i in range(number)]
        teachers = [Teacher.generate_teacher() for i in range(10)]

        for i in range(number):
            group = Group.generate_group()
            group.starosta = random.choice(students)
            group.teacher = random.choice(teachers)
            group.save()
