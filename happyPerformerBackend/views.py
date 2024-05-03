from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def Home(request):
    return JsonResponse({"data":"Welcome to happy backsideeee hehe"})

@csrf_exempt
def MeetTheTeam(request):
    return JsonResponse({"data":"Meet the team here!"})

def Contact(request):
    return HttpResponse('This is the Contact Page of the Happy Performer Backend!')

def About(request):
    return HttpResponse('This is the About Page of the Happy Performer Backend!')

def Login(request):
    return HttpResponse('This is the Login Page of the Happy Performer Backend!')

def Register(request):
    return HttpResponse('This is the Register Page of the Happy Performer Backend!')
