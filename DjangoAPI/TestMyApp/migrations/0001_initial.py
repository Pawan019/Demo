# Generated by Django 5.1.3 on 2024-11-19 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('DepartmentID', models.AutoField(primary_key=True, serialize=False)),
                ('DepartmentName', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('EmployeeID', models.AutoField(primary_key=True, serialize=False)),
                ('EmployeeName', models.CharField(max_length=500)),
                ('DepartmentName', models.CharField(max_length=500)),
                ('DateOfJoining', models.DateField()),
                ('PhotoName', models.CharField(max_length=500)),
            ],
        ),
    ]
