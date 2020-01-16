from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from teachers.models import Teacher
from django.db.models import Q
from teachers.forms import TeachersAddForm


def generate_teacher(request):
    teacher = Teacher.generate_teacher()
    return HttpResponse(f'{teacher.get_info()}')


def teachers(request):
    queryset = Teacher.objects.all()
    response = ''

    filtr_param = request.GET.get('filtr_param')
    if filtr_param:
        queryset = queryset.filter(
            Q(first_name__contains=filtr_param) | Q(last_name__contains=filtr_param) | Q(email__contains=filtr_param)
        )
        # __contains --> like '%blabla%'
        # __endswith --> like '%blabla'
        # __startswith --> like 'blabla%'
        # __istarts/ends/--> регистронезависимый поиск

    for teacher in queryset:
        response += teacher.get_info() + '<br>'
    return render(request,
                  'teachers_list.html',
                  context={'teachers_list': response})


def teacher_add(request):
    if request.method == 'POST':
        form = TeachersAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/teachers/')
    else:
        form = TeachersAddForm()

    return render(request,
                  'teacher_add.html',
                  context={'form': form})