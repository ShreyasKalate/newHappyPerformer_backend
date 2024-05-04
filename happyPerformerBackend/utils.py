from .models import company, department, employee

def create_company_with_departments_and_employees(name, addr, phone, dept_name, emp_name, emp_email, emp_phone, emp_skills):
    try:
        new_company = company.objects.create(c_name=name, c_addr=addr, c_phone=phone)
        new_company.save()
        c_id = new_company.c_id

        new_dept = department.objects.create(d_name=dept_name, c_id=c_id)
        new_dept.save()

        dept_id = new_dept.d_id

        new_employee = employee.objects.create(emp_name=emp_name, emp_emailid=emp_email, emp_skills=emp_skills, emp_role='Super Manager', emp_phone=emp_phone, d_id=dept_id)
        new_employee.save()

    except Exception as e:
        return False, str(e)


