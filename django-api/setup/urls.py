from django.contrib import admin
from django.urls import path,include
from globant.views import hired_employeesViewSets, departmentsViewSets, jobsViewSets
from rest_framework import routers

router = routers.DefaultRouter()
router.register('hired_employees', hired_employeesViewSets, basename='hiredEmployees')
router.register('departments', departmentsViewSets, basename='departments')
router.register('jobs', jobsViewSets, basename='jobs')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls) )
]

