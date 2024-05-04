from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from django.views.decorators.csrf import csrf_exempt

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

def Login(request):
    return HttpResponse('This is the Login Page of the Happy Performer Backend!')

def Register(request):
    return HttpResponse('This is the Register Page of the Happy Performer Backend!')

