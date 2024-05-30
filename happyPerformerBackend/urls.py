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
    path('Users/', views.Users, name='Users'),
    path('logout/', views.Logout, name='logout'),
    path('register/', views.Register, name='register'),
    path('TermsAndConditions/', views.TermsAndConditions, name='terms'),
    path('EmployeeMaster/', views.EmployeeMaster, name='employeemaster'),
    path('SopAndPolicies/', views.SopAndPolicies, name='soppolicies'),
    path('UpdateSelfratings/<int:sop_id>', views.UpdateSelfratings, name='UpdateSelfratings'),
    path('ApplyLeave', views.ApplyLeave, name='ApplyLeave'),
    path('LeaveHistory', views.LeaveHistory, name='LeaveHistory'),
    path('AddLoan', views.AddLoan, name='AddLoan'),
    path('AddExpenses', views.AddExpenses, name='AddExpenses'),
    path('ManageExpenses/', views.ManageExpenses, name='ManageExpenses'),
    path('ExpenseReport', views.ExpenseReport, name='ExpenseReport'),
    path('AddCourses/', views.AddCourses, name='AddCourses'),
    path('UploadMedia/', views.UploadMedia, name='UploadMedia'),
    path('UploadPdf/', views.UploadPdf, name='UploadPdf'),
    path('AddMediaContent/', views.AddMediaContent, name='AddMediaContent'),
    path('UpdateDeleteMedia/', views.UpdateDeleteMedia, name='UpdateDeleteMedia'),
    path('UpdateMedia/<int:course_id>', views.UpdateMedia, name='UpdateMedia'),
    path('ReportingStructureForm', views.ReportingStructureForm, name='ReportingStructureForm'),
    path('CeoHrAnnouncements', views.CeoHrAnnouncements, name='CeoHrAnnouncements'),
    path('AddNewEmployee', views.AddNewEmployee, name='AddNewEmployee'),
    path('EmployeeDetails', views.EmployeeDetails, name='EmployeeDetails'),
    path('AttendanceDetails', views.AttendanceDetails, name='AttendanceDetails'),
    path('LeaveDashboard', views.LeaveDashboard, name='LeaveDashboard'),
    path('LeaveDetails', views.LeaveDetails, name='LeaveDetails'),
    path('ManageLeaveType', views.ManageLeaveType, name='ManageLeaveType'),
    path('EditLeaveType/<int:id>/', views.EditLeaveType, name='EditLeaveType'),
    path('Leaves', views.Leaves, name='Leaves'),
    path('PendingLeaves', views.PendingLeaves, name='PendingLeaves'),
    path('ApprovedLeaves', views.ApprovedLeaves, name='ApprovedLeaves'),
    path('RejectedLeaves', views.RejectedLeaves, name='RejectedLeaves'),
    path('ResignationView', views.ResignationView, name='ResignationView'),
    path('DisplayTraining', views.DisplayTraining, name='DisplayTraining'),
    path('CreateCase', views.CreateCase, name='CreateCase'),
    path('MyCases', views.MyCases, name='MyCases'),
    path('UpdatePersonalDetails', views.UpdatePersonalDetails, name='UpdatePersonalDetails'),
    path('AllCases', views.AllCases, name='AllCases'),
    path('CaseInfo', views.CaseInfo, name='CaseInfo'),
    path('BenefitsCases', views.BenefitsCases, name='BenefitsCases'),
    path('TravelExpenseCases', views.TravelExpenseCases, name='TravelExpenseCases'),
    path('CompensationPayrollCases', views.CompensationPayrollCases, name='CompensationPayrollCases'),
    # path('ManagerRating', views.ManagerRating, name='ManagerRating'),
    path('faqsview', views.FAQManagement, name='faq_management'),
    path('EnrollEmployee', views.EnrollEmployee, name='EnrollEmployee'),
    path('ViewAllEnrollments', views.ViewAllEnrollments, name='ViewAllEnrollments'),
    path('AdhocPayments', views.AdhocPayments, name='AdhocPayments'),
    path('LoanPayments', views.LoanPayments, name='LoanPayments'),
    path('LeaveEncashment', views.LeaveEncashment, name='LeaveEncashment'),
    path('ViewLeaveEncashment', views.ViewLeaveEncashment, name='ViewLeaveEncashment'),
    path('OffCyclePayments', views.OffCyclePayments, name='OffCyclePayments'),
    path('BankTransferPayout', views.BankTransferPayout, name='BankTransferPayout'),
    path('BankTransfer', views.BankTransfer, name='BankTransfer'),
    path('BankTransferUpdate', views.BankTransferUpdate, name='BankTransferUpdate'),
    path('CashChequeTransferPayout', views.CashChequeTransferPayout, name='CashChequeTransferPayout'),
    path('HoldSalaryPayout', views.HoldSalaryPayout, name='HoldSalaryPayout'),
    path('HoldSalary/', views.HoldSalary, name='HoldSalary'),
    path('UnholdSalary/', views.UnholdSalary, name='UnholdSalary'),
    path('PayslipPayout', views.PayslipPayout, name='PayslipPayout'),
    path('GeneratePayslip/', views.GeneratePayslip, name='GeneratePayslip'),
    path('HomeSalary', views.HomeSalary, name='HomeSalary'),
    path('SalaryRevisionHistory', views.SalaryRevisionHistory, name='SalaryRevisionHistory'),
    path('DisplaySalaryDetails', views.DisplaySalaryDetails, name='DisplaySalaryDetails'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
