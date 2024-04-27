from django.shortcuts import render
from django.http import HttpResponse

def Home(request):
    return HttpResponse('This is the Home Page of the Happy Performer Backend!')

def MeetTheTeam(request):
    return HttpResponse('This is the Meet the Team Page of the Happy Performer Backend!')

def Contact(request):
    return HttpResponse('This is the Contact Page of the Happy Performer Backend!')

def About(request):
    return HttpResponse('This is the About Page of the Happy Performer Backend!')

def Login(request):
    return HttpResponse('This is the Login Page of the Happy Performer Backend!')

def Register(request):
    return HttpResponse('This is the Register Page of the Happy Performer Backend!')
