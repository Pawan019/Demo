from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser # to parse the incoming-data into DataModel
from django.http.response import JsonResponse
#import the models we have created
from TestMyApp.models import Departments, Employees
#import the sealizer clases
from TestMyApp.serializer import DepartementsSerializers, EmployeesSerializers

from django.core.files.storage import default_storage

# Create your views here.

#writeing the API Methods for Department Tables
@csrf_exempt
def DepartmentAPI(request, id=0):
    if request.method=='GET': # return all the data in JSON Format
        department = Departments.objects.all()
        departement_Serializers = DepartementsSerializers(department, many=True) #using searializer class into JSON format
        return JsonResponse(departement_Serializers.data, safe=False) # keepinf the safe=False to inform the django that it is fine if there is some issue in the format
    #use the post method to insert the new records into the Database
    elif request.method =='POST':
        department_Data = JSONParser().parse(request)
        departement_Serializers = DepartementsSerializers(data=department_Data)
        if departement_Serializers.is_valid():
            departement_Serializers.save()
            return JsonResponse("Record Added Successfully", safe=False)
        return JsonResponse("Failed to Add the record", safe=False)
    elif request.method =='PUT':
        department_Data = JSONParser().parse(request)
        department = Departments.objects.get(DepartmentID = department_Data['DepartmentID'])
        departement_Serializers = DepartementsSerializers(department, data=department_Data)
        if departement_Serializers.is_valid():
            departement_Serializers.save()
            return JsonResponse("Record Updated Successfully", safe=False)
        return JsonResponse("Record Updation Failed", safe=False)
    elif request.method =='DELETE':
        department = Departments.objects.get(DepartmentID = id) #the id will be provided eith url
        department.delete()
        return JsonResponse("Record Deleted Successfully", safe=False)

@csrf_exempt
def employeeApi(request,id=0):
    if request.method=='GET':
        employees = Employees.objects.all()
        employees_serializer=EmployeesSerializers(employees,many=True)
        return JsonResponse(employees_serializer.data,safe=False)
    elif request.method=='POST':
        employee_data=JSONParser().parse(request)
        employees_serializer=EmployeesSerializers(data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        employee_data=JSONParser().parse(request)
        employee=Employees.objects.get(EmployeeID=employee_data['EmployeeID'])
        employees_serializer=EmployeesSerializers(employee,data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        employee=Employees.objects.get(EmployeeID=id)
        employee.delete()
        return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def SaveFile(request):
    file=request.FILES['file']
    file_name=default_storage.save(file.name,file)
    return JsonResponse(file_name,safe=False)
