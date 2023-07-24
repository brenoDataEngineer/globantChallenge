from rest_framework import serializers
from globant.models import hired_employees, departments, jobs

class hired_employees_serializer(serializers.ModelSerializer):
    class Meta:
        model = hired_employees
        fields = ['id','name', 'datetime', 'department_id', 'job_id']

class departments_serializer(serializers.ModelSerializer):
    class Meta:
        model = departments
        fields = ['id','department']

class jobs_serializer(serializers.ModelSerializer):
    class Meta:
        model = jobs
        fields = ['id','job']