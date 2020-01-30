from django.contrib import admin
from teachers.models import Teacher
from teachers.forms import TeachersAdminForm


class TeacherAdmin(admin.ModelAdmin):
    # readonly_fields = ('email', 'telephone')
    list_display = ('first_name', 'last_name', 'birth_date',
                    'email', 'telephone')
    list_per_page = 20
    form = TeachersAdminForm


admin.site.register(Teacher, TeacherAdmin)
