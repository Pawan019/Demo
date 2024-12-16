from django.db import models

# Create your models here.
class Departments(models.Model):
    DepartmentID = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=500)

class Employees(models.Model):
    EmployeeID = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=500)
    DepartmentName = models.CharField(max_length=500)
    DateOfJoining = models.DateField()
    PhotoName = models.CharField(max_length=500)
