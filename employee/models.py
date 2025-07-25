from django.db import models
from mongoengine import Document, StringField, DateTimeField

class Departments(Document):
    DepartmentName = StringField(max_length=500)

class Employees(Document):
    EmployeeName = StringField(max_length=500)
    Department = StringField(max_length=500)
    DateOfJoining = DateTimeField()
    PhotoFileName = StringField(max_length=500)
