from django.contrib import admin
from students.models import Student, Group


class StudentAdmin(admin.ModelAdmin):
    readonly_fields = ('email', 'telephone')
    list_display = ('id', 'first_name', 'last_name',
                    'email', 'group_id')
    list_select_related = ('group_id', )
    list_per_page = 20

    def get_readonly_fields(self, request, obj=None):
        # from pdb import set_trace
        # set_trase()
        if request.user.groups.filter(name='manager').exists():
            return('email', 'telephone')
        return()


class StudentInline(admin.TabularInline):
    model = Student
    raw_id_fields = ('group_id', )


class GroupAdmin(admin.ModelAdmin):
    # readonly_fields = ('student_cnt')
    list_display = ('group_id', 'student_cnt', 'teacher',
                    'starosta')
    list_select_related = ('teacher', 'starosta', )
    list_per_page = 20
    inlines = [
        StudentInline
    ]


admin.site.register(Student, StudentAdmin)
admin.site.register(Group, GroupAdmin)




