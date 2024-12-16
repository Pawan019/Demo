from rest_framework import serializers
from TestMyApp.models import Departments, Employees

class DepartementsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ('DepartmentID', 'DepartmentName')

class EmployeesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('EmployeeID', 'EmployeeName', 'DepartmentName', 'DateOfJoining', 'PhotoName')