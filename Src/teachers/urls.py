from django.contrib import admin
from django.urls import path

from teachers.views import generate_teacher, teachers, teachers_add, teachers_edit


urlpatterns = [
    path('generate-teacher/', generate_teacher, name='generate-teacher'),
    path('teachers/', teachers, name='teachers'),
    path('teachers/add/', teachers_add, name='teachers-add'),
    path('teachers/edit/<int:pk>/', teachers_edit, name='teachers-edit'),
]