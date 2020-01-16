from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
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


def teachers_add(request):
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


def teachers_edit(request, pk):
    try:
        teacher = Teacher.objects.get(id=pk)
    except Teacher.DoesNotExist:
        return HttpResponseNotFound(f'Teacher with id {pk} not found')

    if request.method == 'POST':
        form = TeachersAddForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teachers'))
    else:
        form = TeachersAddForm(instance=teacher)

    return render(request,
                  'teacher_edit.html',
                  context={'form': form, 'pk': pk})
