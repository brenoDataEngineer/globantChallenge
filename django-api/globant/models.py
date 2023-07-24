from django.db import models

class hired_employees(models.Model):
    id = models.CharField(max_length=5, primary_key=True)
    name = models.CharField(max_length=30)
    datetime = models.DateField()
    department_id = models.CharField(max_length=3)
    job_id = models.CharField(max_length=3)

    def __str__(self):
        return self.name
    
class departments(models.Model):
    id = models.CharField(max_length=5, primary_key=True)
    department = models.CharField(max_length=30)
    def __str__(self):
        return self.department
    
class jobs(models.Model):
    id = models.CharField(max_length=5, primary_key=True)
    job = models.CharField(max_length=30)
    def __str__(self):
        return self.job