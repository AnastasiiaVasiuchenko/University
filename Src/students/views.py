from django.shortcuts import render
from django.http import  HttpResponse
from students.models import Student


def generate_student(request):
    student = Student.generate_student()
    return HttpResponse(f'{student.get_info()}')



