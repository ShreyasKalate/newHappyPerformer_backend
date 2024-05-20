from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('meet-the-team/', views.MeetTheTeam, name='meet-the-team'),
    path('contact/', views.Contact, name='contact'),
    path('about/', views.About, name='about'),
    path('login/', views.Login, name='login'),
    path('register/', views.Register, name='register'),
    path('terms/', views.TermsAndConditions, name='terms'),
    path('employee-master/', views.Employee_Master, name='employeemaster'),
    path('soppolicies/', views.SopAndPolicies, name='soppolicies'),
    path('tasks/<int:sop_id>/', views.update_selfratings, name='update_selfratings'),
    path('AddCourses/', views.AddCourses, name='AddCourses'),
    path('UploadMedia/', views.UploadMedia, name='UploadMedia'),
    path('UploadPdf/', views.UploadPdf, name='UploadPdf'),
    path('AddMediaContent/', views.AddMediaContent, name='AddMediaContent'),
    path('UpdateDeleteMedia/', views.UpdateDeleteMedia, name='UpdateDeleteMedia'),
    path('UpdateMedia/<int:course_id>', views.UpdateMedia, name='UpdateMedia'),
    path('EmployeeDetails/', views.EmployeeDetails, name='EmployeeDetails'),
    path('AttendanceDetails/', views.AttendanceDetails, name='AttendanceDetails'),
    path('LeaveDashboard/', views.LeaveDashboard, name='LeaveDashboard'),
    path('LeaveDetails/', views.LeaveDetails, name='LeaveDetails'), 
]
