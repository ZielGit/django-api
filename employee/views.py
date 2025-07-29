from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from employee.models import Departments, Employees
import json
from django.core.files.storage import default_storage

@csrf_exempt
def create_department(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        department = Departments(**data)
        department.save()
        return JsonResponse({'id': str(department.id)}, status=201)

def list_departments(request):
    departments = Departments.objects()
    data = [e.to_mongo().to_dict() for e in departments]
    for d in data:
        d['id'] = str(d.pop('_id'))
    return JsonResponse(data, safe=False)

def get_department(request, dep_id):
    try:
        department = Departments.objects.get(id=dep_id)
        data = department.to_mongo().to_dict()
        data['id'] = str(data.pop('_id'))
        return JsonResponse(data)
    except Departments.DoesNotExist:
        return JsonResponse({'error': 'Departamento no encontrado'}, status=404)

@csrf_exempt
def update_department(request, dep_id):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            department = Departments.objects.get(id=dep_id)
            department.update(**data)
            return JsonResponse({'message': 'Departamento actualizado'})
        except Departments.DoesNotExist:
            return JsonResponse({'error': 'Departamento no encontrado'}, status=404)

@csrf_exempt
def delete_department(request, dep_id):
    if request.method == 'DELETE':
        try:
            department = Departments.objects.get(id=dep_id)
            department.delete()
            return JsonResponse({'message': 'Departamento eliminado'})
        except Departments.DoesNotExist:
            return JsonResponse({'error': 'Departamento no encontrado'}, status=404)

@csrf_exempt
def create_employee(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        employee = Employees(**data)
        employee.save()
        return JsonResponse({'id': str(employee.id)}, status=201)

def list_employees(request):
    employees = Employees.objects()
    data = [e.to_mongo().to_dict() for e in employees]
    for d in data:
        d['id'] = str(d.pop('_id'))
    return JsonResponse(data, safe=False)

def get_employee(request, emp_id):
    try:
        employee = Employees.objects.get(id=emp_id)
        data = employee.to_mongo().to_dict()
        data['id'] = str(data.pop('_id'))
        return JsonResponse(data)
    except Employees.DoesNotExist:
        return JsonResponse({'error': 'Empleado no encontrado'}, status=404)

@csrf_exempt
def update_employee(request, emp_id):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            employee = Employees.objects.get(id=emp_id)
            employee.update(**data)
            return JsonResponse({'message': 'Empleado actualizado'})
        except Employees.DoesNotExist:
            return JsonResponse({'error': 'Empleado no encontrado'}, status=404)

@csrf_exempt
def delete_employee(request, emp_id):
    if request.method == 'DELETE':
        try:
            employee = Employees.objects.get(id=emp_id)
            employee.delete()
            return JsonResponse({'message': 'Empleado eliminado'})
        except Employees.DoesNotExist:
            return JsonResponse({'error': 'Empleado no encontrado'}, status=404)

@csrf_exempt
def save_file(request):
    if request.method == 'POST':
        file = request.FILES['file']
        file_name = default_storage.save(file.name, file)
        return JsonResponse({'file_name': file_name}, status=201)
