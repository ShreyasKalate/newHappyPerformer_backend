from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Home, name='home'),
    path('meet-the-team/', views.MeetTheTeam, name='meet-the-team'),
    path('contact/', views.Contact, name='contact'),
    path('about/', views.About, name='about'),
    path('login/', views.Login, name='login'),
    path('logout/', views.Logout, name='logout'),
    path('register/', views.Register, name='register'),
    path('TermsAndConditions/', views.TermsAndConditions, name='terms'),
    path('EmployeeMaster/', views.EmployeeMaster, name='employeemaster'),
    path('SopAndPolicies/', views.SopAndPolicies, name='soppolicies'),
    path('UpdateSelfratings/<int:sop_id>', views.UpdateSelfratings, name='UpdateSelfratings'),
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
    path('ManageLeaveType/', views.ManageLeaveType, name='ManageLeaveType'),
    path('EditLeaveType/<int:id>/', views.EditLeaveType, name='EditLeaveType'),
    path('Leaves/', views.Leaves, name='Leaves'),
    path('PendingLeaves/', views.PendingLeaves, name='PendingLeaves'),
    path('ApprovedLeaves/', views.ApprovedLeaves, name='ApprovedLeaves'),
    path('RejectedLeaves/', views.RejectedLeaves, name='RejectedLeaves'),
    path('ResignationView/', views.ResignationView, name='ResignationView'),
    path('DisplayTraining/', views.DisplayTraining, name='DisplayTraining'),
    path('CreateCase', views.CreateCase, name='CreateCase'),
    path('MyCases/', views.MyCases, name='MyCases'),
    path('faqsview/', views.FAQManagement, name='faq_management'),
    path('EnrollEmployee', views.EnrollEmployee, name='EnrollEmployee'),
    path('ViewAllEnrollments', views.ViewAllEnrollments, name='ViewAllEnrollments'),
    path('BankTransferPayout', views.BankTransferPayout, name='BankTransferPayout'),
    path('BankTransfer', views.BankTransfer, name='BankTransfer'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
