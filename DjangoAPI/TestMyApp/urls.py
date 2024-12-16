from django.urls import re_path, path
from TestMyApp import views

from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('Departments', views.DepartmentAPI), 
    re_path('Departments/([0-9]+)', views.DepartmentAPI), 

    path('Employee', views.employeeApi), 
    re_path('Employee/([0-9]+)', views.employeeApi),
    re_path('Employee/savefile',views.SaveFile)
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)