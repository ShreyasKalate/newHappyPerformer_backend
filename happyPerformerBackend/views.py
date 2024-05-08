import json
from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.contrib.auth import authenticate
from django.db.models import F, Prefetch, OuterRef, Subquery
from django.contrib.auth.models import User

@csrf_exempt
def Home(request):
    return JsonResponse({"data":"Welcome to happy backsideeee hehe"})

@csrf_exempt
def MeetTheTeam(request):
    return JsonResponse({"data":"Meet the team here!"})

@csrf_exempt
def Contact(request):
    return JsonResponse({"data":"Contact Us Page reached without any issues"})

@csrf_exempt
def About(request):
    return JsonResponse({"data":"About Us Page reached without any issues"})

@csrf_exempt
def TermsAndConditions(request):
    return JsonResponse({"data":"Terms and Conditions Page reached without any issues"})

@csrf_exempt
def Login(request):
    if request.method == 'POST':
        data = request.POST

        email = data.get('email')
        password = data.get('password')

        User = authenticate(emp_emailid=email, emp_pwd=password)

        if User is not None:
            return JsonResponse({'message': 'Login successful'}, status=200)
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=401)

    return JsonResponse({'error': 'Invalid credentials'}, status=401)

@csrf_exempt
def Register(request):
    if request.method == 'POST':
        data = request.POST
        print(data)

        name = data.get('companyName')
        addr = data.get('companyAddress')
        phone = data.get('companyPhone')
        dept_name = data.get('deptName')
        emp_name = data.get('empName')
        emp_email = data.get('empEmail')
        emp_phone = data.get('empPhone')
        emp_skills = data.get('empSkills')

        new_company = Company.objects.create(c_name=name, c_addr=addr, c_phone=phone)
        new_company.save()
        c_id = new_company.c_id

        new_dept = Department.objects.create(d_name=dept_name, c_id=c_id)
        new_dept.save()
        dept_id = new_dept.d_id

        new_employee = Employee.objects.create(emp_name=emp_name, emp_emailid=emp_email, emp_skills=emp_skills, emp_role='Super Manager', emp_phone=emp_phone, d_id=dept_id)
        new_employee.save()

        return JsonResponse({'message': 'Company views registration successful'}, status=201)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)

@csrf_exempt
def Employee_Master(request):

    employees = Employee.objects.all().values('emp_name', 'emp_emailid', 'emp_phone', 'd_id')
    departments = Department.objects.all().values('d_name','d_id')

    data = {
        'employees': list(employees),
        'departments': list(departments)
    }
    
    return JsonResponse(data)
