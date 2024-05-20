import json
from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db import transaction
from django.core import serializers
from django.db import connection


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
        data = json.loads(request.body)

        name = data.get('companyName')
        addr = data.get('companyAddress')
        phone = data.get('companyPhone')
        dept_names_str = data.get('deptName')
        dept_names = [name.strip() for name in dept_names_str.split(',')]
        emp_name = data.get('empName')
        emp_email = data.get('empMail')
        emp_phone = data.get('empNum')
        emp_skills = data.get('empSkills')

        new_company = Company.objects.create(c_name=name, c_addr=addr, c_phone=phone)

        company_id = Company.objects.order_by('-pk').first()

        first_dept_id = None
        for dept_name in dept_names:
            new_dept = Department.objects.create(d_name=dept_name, c_id=company_id)
            if first_dept_id is None:
                first_dept_id = Department.objects.order_by('-pk').first()

        Employee.objects.create(emp_name=emp_name, emp_emailid=emp_email, emp_skills=emp_skills, emp_role='HR', emp_phone=emp_phone, d_id=first_dept_id)

        return JsonResponse({'message': 'Company registration successful'}, status=201)
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


@csrf_exempt
def Profile(request, id):
    try:
        personal_details =  personal_details.objects.filter(mail=id).values()
        if not personal_details.exists():
            return JsonResponse({'error': 'Employee Details not found'}, status=404)
        return JsonResponse(list(personal_details), safe=False)
    except Exception as e:
        print("Error fetching employee data:", e)
        return JsonResponse({'error': 'Internal Server Error'}, status=500)



@csrf_exempt
def SopAndPolicies(request):
    # id = request.user.email
    eid = 'abc@gmail.com'

    #Tables needed
    # tasks= ratings, remark, selfratings (emp_emailid, pk:task_id, fk:sop_id)
    # sop table= sop_id, type, s_name, sdate
    # files table= file_name (fk: sop_id, pk:id)

    tasks_data = Tasks.objects.filter(emp_emailid=eid).values('ratings', 'remark', 'sop_id', 'selfratings')

    sop_ids = [task['sop_id'] for task in tasks_data]
    sop_data = Sop.objects.filter(sop_id__in=sop_ids).values('sop_id', 'type', 's_name', 'sdate')

    files_data = Files.objects.filter(sop_id__in=sop_ids).values('file_name')

    data = {
        'tasks': list(tasks_data),
        'sop': list(sop_data),
        'files': list(files_data)
    }
    return JsonResponse(data, safe=False)

@csrf_exempt
@require_http_methods(["PUT"])
def update_selfratings(request, sop_id):
    try:
        # Retrieve the task object
        task = Tasks.objects.get(sop_id = sop_id)

        # Update the ratings field
        data = json.loads(request.body)
        self_rating = int(data.get('selfratings'))
        task.selfratings = self_rating
        task.save()

        return JsonResponse({'message': 'Rating updated successfully'}, status=200)
    except Tasks.DoesNotExist:
        return JsonResponse({'error': 'Task does not exist'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


@csrf_exempt
def AddCourses(request):
    if request.method == 'POST':
        try:
            if request.content_type == 'application/json':
                data = json.loads(request.body)
                course_title = data.get('course_title')
                description = data.get('description')
                # thumbnail = request.FILES.get('thumbnail')
            else:
                # Handle form data or file uploads
                course_title = request.POST.get('course_title')
                description = request.POST.get('description')
                # thumbnail = request.FILES.get('thumbnail')

            course = Courses.objects.create(
                course_title=course_title,
                description=description,
                thumbnail='demo',
                # Hardcoded c_id and c_name for now
                c_id=1,
                c_name='Some Name'
            )

            response_data = {
                'message': 'Course added successfully',
                'course_id': course.course_id
            }

            return JsonResponse({'message': 'Course added successfully', 'course_id': course.course_id}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)


@csrf_exempt
def UploadMedia(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            # video_name = data.get('video_name')
            location = data.get('location')
            descr = data.get('descr')
            course_id = data.get('course_id')

            existing_videos_count = Video.objects.filter(course_id=course_id).count()
            if existing_videos_count > 1:
                return JsonResponse({'message': 'Video with the same details already exists.'}, status=400)

            video = Video.objects.create(
                location=location,
                descr=descr,
                course_id=course_id,
                # video_name=video_name
            )

            return JsonResponse({'message': 'Video added successfully'}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)


@csrf_exempt
def UploadPdf(request):
    if request.method == 'POST':
        try:
            pdf_file = request.FILES.get('pdf_file')
            pdf_name=pdf_file.name
            pdf_description = request.POST.get('pdf_description')
            course_id = request.POST.get('course_id')

            # Create a new PDF object
            pdf = Pdf.objects.create(
                # pdf_file=pdf_file,
                pdf_name=pdf_name,
                location=pdf_name,
                descr=pdf_description,
                course_id=course_id
            )

            return JsonResponse({'message': 'PDF uploaded successfully'}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)


@csrf_exempt
def AddMediaContent(request):
    # Get the company id (c_id and email from session)
    # Hardcoded values as of now
    c_id = 1
    courses_data = Courses.objects.filter(c_id=c_id).values('course_title', 'course_id')

    data = list(courses_data)

    return JsonResponse(data, safe=False)


@csrf_exempt
def UpdateDeleteMedia(request):
    # Get the company id (c_id and email from session)
    # Hardcoded values as of now
    c_id = 1
    courses_data = Courses.objects.filter(c_id=c_id).values('course_title', 'description', 'course_id')
    data = list(courses_data)
    return JsonResponse(data, safe=False)


@csrf_exempt
def UpdateMedia(request, course_id):
    if request.method == 'GET':
        try:
            course = Courses.objects.get(course_id=course_id)
            videos = Video.objects.filter(course_id=course_id).values('video_id', 'location', 'descr')

            course_data = {
                'course_id': course.course_id,
                'course_title': course.course_title,
                'videos': list(videos)
            }
            return JsonResponse(course_data, safe=False)
        except Courses.DoesNotExist:
            return JsonResponse({'error': 'Course not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    elif request.method == 'PUT':
        try:
            data = json.loads(request.body)
            course = Courses.objects.get(course_id=course_id)

            if 'course_title' in data:
                course.course_title = data['course_title']
                course.save()

            if 'videos' in data:
                for video_data in data['videos']:
                    video_id = video_data.get('video_id')
                    if video_id:
                        video = Video.objects.get(video_id=video_id, course_id=course_id)
                        video.location = video_data.get('location', video.location)
                        video.descr = video_data.get('descr', video.descr)
                        video.save()

            return JsonResponse({'message': 'Course updated successfully'}, status=200)
        except (Courses.DoesNotExist, Video.DoesNotExist):
            return JsonResponse({'error': 'Course or video not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    elif request.method == 'DELETE':
        try:
            media_content = Courses.objects.get(course_id=course_id)
            media_content.delete()
            return JsonResponse({'message': 'Media content deleted successfully'})
        except Courses.DoesNotExist:
            return JsonResponse({'error': 'Media content not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    else:
        return JsonResponse({'error': 'Unsupported method'}, status=405)


@csrf_exempt
def EmployeeDetails(request):
    # Hardcoded company ID for now
    c_id = 81

    if request.method == 'GET':
        try:
            departments = Department.objects.filter(c_id=c_id).values('d_name', 'd_id')
            dept_id = [d['d_id'] for d in departments]
            employees = Employee.objects.filter(d_id__in=dept_id).values('emp_name', 'emp_emailid', 'emp_phone', 'd_id', 'emp_role')
            data = {
                'employees': list(employees)
            }
            return JsonResponse(data)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    elif request.method == 'DELETE':
        emp_emailid = request.GET.get('emp_emailid')
        if not emp_emailid:
            return JsonResponse({'error': 'Employee email ID is required'}, status=400)
        try:
            employee = Employee.objects.get(emp_emailid=emp_emailid)
            employee.delete()
            return JsonResponse({'message': 'Employee deleted successfully'})
        except Employee.DoesNotExist:
            return JsonResponse({'error': 'Employee not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    else:
        return JsonResponse({'error': 'Unsupported method'}, status=405)

from django.http import JsonResponse


@csrf_exempt
def AttendanceDetails(request):
    # Hardcoded company ID for now
    c_id = 81

    if request.method == 'GET':
        try:
            departments = Department.objects.filter(c_id=c_id).values_list('d_id', flat=True)
            employees = Employee.objects.filter(d_id__in=departments).values('emp_emailid')
            emp_emails = [e['emp_emailid'] for e in employees]
            attendance_data = Attendance.objects.filter(emp_emailid__in=emp_emails).values('id','datetime_log', 'log_type', 'emp_emailid')

            data = []
            for attendance in attendance_data:
                data.append({
                    'id': attendance['id'],
                    'emp_email': attendance['emp_emailid'],
                    'date': attendance['datetime_log'],
                    'log_type': attendance['log_type'],
                    'time': attendance['datetime_log']
                })
            return JsonResponse({'data': data})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    elif request.method == 'DELETE':
        id = request.GET.get('id')
        if not id:
            return JsonResponse({'error': 'Attendance ID is required'}, status=400)
        try:
            attendance = Attendance.objects.get(id=id)
            attendance.delete()
            return JsonResponse({'message': 'Attendance record deleted successfully'})
        except Attendance.DoesNotExist:
            return JsonResponse({'error': 'Attendance record not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    else:
        return JsonResponse({'error': 'Unsupported method'}, status=405)
    

def LeaveDashboard(request):
    if request.method == 'GET':
        # Need to fetch company id. Hardcoded as of now
        company_id = 81

        empcount = Employee.objects.filter(d_id__c_id=company_id).count()
        dptcount = Department.objects.filter(c_id=company_id).count()
        leavtypcount = Leavetype.objects.count()

        leaves_fetched = Tblleaves.objects.select_related('emp_emailid', 'LeaveType').order_by('-id')

        leaves_data = []
        for leave in leaves_fetched:
            leave_dict = {
                'lid': leave.id,
                'emp_name': leave.emp_emailid.emp_name,
                'emp_emailid': leave.emp_emailid.emp_emailid,
                'LeaveType': leave.LeaveType_id,
                'PostingDate': leave.PostingDate.strftime('%Y-%m-%d %H:%M:%S'),
                'Status': leave.Status,
            }
            leaves_data.append(leave_dict)

        response_data = {
            'empcount': empcount,
            'dptcount': dptcount,
            'leavtypcount': leavtypcount,
            'leaves_fetched': leaves_data,
        }
        return JsonResponse(response_data, safe=False)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
