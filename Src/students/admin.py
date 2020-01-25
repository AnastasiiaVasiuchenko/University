from django.contrib import admin
from students.models import Student


class StudentAdmin(admin.ModelAdmin):
    readonly_fields = ('email', 'telephone')
    list_display = ('id', 'first_name', 'last_name',
                    'email', 'group_id')
    list_select_related = ('group_id', )
    list_per_page = 10

    def get_readonly_fields(self, request, obj=None):
        # from pdb import set_trace
        # set_trase()
        if request.user.groups.filter(name='manager').exists():
            return('email', 'telephone')
        return()


admin.site.register(Student, StudentAdmin)
