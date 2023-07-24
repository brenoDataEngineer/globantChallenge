from django.contrib import admin
from globant.models import hired_employees, departments, jobs

class hired_employeesAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'datetime', 'department_id', 'job_id')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 20

admin.site.register(hired_employees, hired_employeesAdmin)

class departmentsAdmin(admin.ModelAdmin):
    list_display = ('id','department')
    list_display_links = ('id', 'department')
    search_fields = ('department',)
    list_per_page = 20

admin.site.register(departments, departmentsAdmin)

class jobsAdmin(admin.ModelAdmin):
    list_display = ('id','job')
    list_display_links = ('id', 'job')
    search_fields = ('job',)
    list_per_page = 20

admin.site.register(jobs, jobsAdmin)