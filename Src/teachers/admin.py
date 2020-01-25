from django.contrib import admin
from teachers.models import Teacher


class TeacherAdmin(admin.ModelAdmin):
    # readonly_fields = ('email', 'telephone')
    list_display = ('first_name', 'last_name', 'birth_date',
                    'email', 'telephone')
    list_per_page = 20


admin.site.register(Teacher, TeacherAdmin)
