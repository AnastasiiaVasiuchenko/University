from django.db import models
from datetime import datetime
from faker import Faker


class Teacher(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birth_date = models.DateField()
    email = models.EmailField(unique=True)
    # add avatar TODO
    telephone = models.CharField(max_length=30, unique=True)  # clean phone TODO

    def get_info(self):
        return f'{self.first_name} {self.last_name} {self.birth_date} {self.email}'

    @classmethod
    def generate_teacher(cls):
        faker = Faker()
        teacher = cls(
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            birth_date=datetime.now().date(),
            email=faker.email(),
            telephone=faker.phone_number()
        )
        teacher.save()
        return teacher

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


from teachers.signals import *



