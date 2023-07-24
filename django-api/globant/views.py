from rest_framework import viewsets, generics
from globant.models import hired_employees, departments, jobs
from globant.serializer import hired_employees_serializer, departments_serializer, jobs_serializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class hired_employeesViewSets(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas"""
    queryset = hired_employees.objects.all()
    serializer_class = hired_employees_serializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class departmentsViewSets(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas"""
    queryset = departments.objects.all()
    serializer_class = departments_serializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class jobsViewSets(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas"""
    queryset = jobs.objects.all()
    serializer_class = jobs_serializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]