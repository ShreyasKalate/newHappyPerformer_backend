import json
from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import company, department, employee
from .utils import create_company_with_departments_and_employees

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
        try:
            data = json.loads(request.body)
            print(data)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)

        email = data['email']
        password = data['password']

        if email == 'admin' and password == 'admin':
            return JsonResponse({'message': 'Login successful'}, status=200)
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=401)
    return HttpResponse('This is the Login Page of the Happy Performer Backend!')

@csrf_exempt
def Register(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print(data)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)
        
        name = data['companyName']
        addr = data['companyAddress']
        phone = data['companyPhone']
        dept_name = data['deptName']
        emp_name = data['empName']
        emp_email = data['empMail']
        emp_phone = data['empNum']
        emp_skills = data['empSkills']

        create_company_with_departments_and_employees(name, addr, phone, dept_name, emp_name, emp_email, emp_phone, emp_skills)

        return JsonResponse({'message': 'Company views registration successful'}, status=201)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)


