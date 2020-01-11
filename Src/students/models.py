from django.db import models
from datetime import datetime
from  faker import Faker
import random
import string

class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birth_date = models.DateField()
    email = models.EmailField()
    # add avatar TODO
    telephone = models.CharField(max_length=16)  # clean phone TODO
    address = models.CharField(max_length=255, null=True, blank=True)

    def get_info(self):
        return f'{self.first_name} {self.last_name} {self.birth_date}'

    @classmethod
    def generate_student(cls):
        faker = Faker()
        student = cls(
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            birth_date=datetime.now().date(),
            email=faker.email(),
            telephone=faker.phone_number(),
            address=faker.address()
        )
        student.save()
        return student


class Group(models.Model):
    group_id = models.CharField(max_length=3)
    student_cnt = models.IntegerField()
    teacher_name = models.CharField(max_length=50)

    def get_info(self):
        return f'{self.group_id} {self.student_cnt} {self.teacher_name}'


    @classmethod
    def generate_group(cls):
        faker = Faker()
        group = cls(
            group_id=''.join(random.choice(string.ascii_letters + string.digits) for i in range(3)),
            student_cnt=random.randint(3, 10),
            teacher_name=faker.name()
        )
        group.save()
        return group







