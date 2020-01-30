from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from students.models import Student, Group
from students.forms import StudentsAddForm, GroupsAddForm, ContactForm, StudentAdminForm


def generate_student(request):
    student = Student.generate_student()
    return HttpResponse(f'{student.get_info()}')


def students(request):
    queryset = Student.objects.all().select_related('group_id')  # name vneshniy klych
    fn = request.GET.get('first_name')
    if fn:
        queryset = queryset.filter(first_name__contains=fn)
        # __contains --> like '%blabla%'
        # __endswith --> like '%blabla'
        # __startswith --> like 'blabla%'
        # __istarts/ends/--> регистронезависимый поиск
    return render(request,
                  'students_list.html',
                  context={'students': queryset})


def generate_group(request):
    group = Group.generate_group()
    return HttpResponse(f'{group.get_info()}')


def groups(request):
    queryset = Group.objects.all().select_related('teacher', 'starosta')

    grid = request.GET.get('group_id')
    if grid:
        queryset = queryset.filter(group_id__contains=grid)

    return render(request,
                  'groups_list.html',
                  context={'groups': queryset})


def stud_add(request):
    if request.method == 'POST':
        form = StudentsAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students'))
    else:
        form = StudentsAddForm()

    return render(request,
                  'student_add.html',
                  context={'form': form})


def group_add(request):
    if request.method == 'POST':
        form = GroupsAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/groups/')
    else:
        form = GroupsAddForm()

    return render(request,
                  'group_add.html',
                  context={'form': form})


def stud_edit(request, pk):
    from students.forms import StudentsAddForm

    try:
        student = Student.objects.get(id=pk)
    except Student.DoesNotExist:
        return HttpResponseNotFound(f'Student with id {pk} not found')

    if request.method == 'POST':
        form = StudentsAddForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students'))
    else:
        form = StudentsAddForm(instance=student)

    return render(request,
                  'student_edit.html',
                  context={'form': form, 'pk': pk})


def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            with open('log.txt', 'a') as log:
                for key, value in form.cleaned_data.items():
                    log.write('{}:{}\n'.format(key, value))
                log.write('\n')
            return HttpResponseRedirect(reverse('contact'))
    else:
        form = ContactForm()

    return render(request,
                  'contact.html',
                  context={'form': form})


def group_edit(request, pk):

    try:
        group = Group.objects.get(id=pk)
    except Group.DoesNotExist:
        return HttpResponseNotFound(f'Group with id {pk} not found')

    if request.method == 'POST':
        form = GroupsAddForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups'))
    else:
        form = GroupsAddForm(instance=group)

    return render(request,
                  'group_edit.html',
                  context={'form': form, 'pk': pk})
