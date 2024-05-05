from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser

class Company(models.Model):
    c_id = models.BigAutoField(primary_key=True)
    c_name = models.CharField(max_length=30, null=True)
    c_addr = models.CharField(max_length=50, null=True, default=None)
    c_phone = models.BigIntegerField()
    add_date = models.CharField(max_length=200, null=True, default=None)
    pay_sts = models.CharField(max_length=200, null=True, default=None)
    payment_type = models.CharField(max_length=100, null=True, default=None)
    start_date = models.TextField(null=True, default=None)
    end_date = models.TextField(null=True, default=None)
    emp_limit = models.IntegerField(null=True, default=None)
    storage_limit = models.IntegerField(null=True, default=None)
    storage_used = models.IntegerField(null=True, default=None)

class Department(models.Model):
    d_id = models.BigAutoField(primary_key=True)
    d_name = models.CharField(max_length=20)
    add_date = models.CharField(max_length=200, null=True, default=None)
    c_id = models.ForeignKey(Company, on_delete=models.CASCADE, db_column='c_id')
    class Meta:
        indexes = [
            models.Index(fields=['d_name', 'c_id'], name='Department_d_name_c_id'),
            models.Index(fields=['c_id'], name='Department_c_id'),
        ]

class Employee(AbstractBaseUser):
    emp_name = models.CharField(max_length=30)
    emp_emailid = models.CharField(max_length=50, primary_key=True, default='A@gmail.com')
    emp_skills = models.CharField(max_length=150)
    emp_role = models.CharField(max_length=50)
    emp_pwd = models.CharField(max_length=15, default='changeme')
    emp_phone = models.CharField(max_length=11)
    emp_profile = models.CharField(max_length=100, default='profile.png')
    d_id = models.IntegerField()
    add_date = models.CharField(max_length=200, null=True, default=None)
    pay_sts = models.CharField(max_length=200, null=True, default=None)
    Status = models.CharField(max_length=8, default='Active')
    likes = models.CharField(max_length=10000, default='0')

    d_id = models.ForeignKey(Department, on_delete=models.CASCADE, db_column='d_id')
    
    USERNAME_FIELD = 'emp_emailid'
    REQUIRED_FIELDS = ['emp_pwd']
    class Meta:
        indexes = [
            models.Index(fields=['d_id'], name='Employee_d_id'),
        ]


class Adhaar(models.Model):
    A_Id = models.BigAutoField(primary_key=True)
    adhaar_no = models.BigIntegerField()
    adhaar_name = models.CharField(max_length=200)
    enroll_no = models.PositiveIntegerField()
    adhaar_pic = models.CharField(max_length=150)
    P_Id = models.ForeignKey(Employee, on_delete=models.CASCADE, db_column='P_Id')

class adhoc(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20 )
    dept = models.CharField(max_length=255)
    type = models.CharField(max_length=20)
    mon = models.CharField(max_length=20)
    year = models.PositiveSmallIntegerField()
    amt = models.IntegerField()


class admintable(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.CharField(max_length=200, null=True, default=None)
    role = models.CharField(max_length=200, null=True, default=None)
    full_name = models.CharField(max_length=200, null=True, default=None)
    user = models.CharField(max_length=255, null=True, default=None)
    password = models.CharField(max_length=255, null=True, default="changeme")
    otp_id = models.CharField(max_length=200, null=True, default=None)
    otp = models.CharField(max_length=200, null=True, default=None)
    status = models.CharField(max_length=200, null=True, default=None)
    user_pics = models.CharField(max_length=200, null=True, default=None)
    created_at = models.CharField(max_length=200, null=True, default=None)
    modified_at = models.CharField(max_length=200, null=True, default=None)


class admin_log(models.Model):
    id = models.BigAutoField(primary_key=True)
    admin_id = models.CharField(max_length=200, null=True, default=None)
    my_ip = models.CharField(max_length=200, null=True, default=None)
    logged_in = models.CharField(max_length=200, null=True, default=None)
    logged_out = models.CharField(max_length=200, null=True, default=None)


class answer(models.Model):
    id = models.BigAutoField(primary_key=True)
    qid = models.TextField()
    ansid = models.TextField()


class ans_static(models.Model):
    id = models.BigAutoField(primary_key=True)
    qid = models.CharField(max_length=50)
    ansid = models.CharField(max_length=50)


class attendance(models.Model):
    id = models.BigAutoField(primary_key=True)
    emp_emailid = models.ForeignKey(Employee, on_delete=models.CASCADE, db_column='emp_emailid')
    log_type = models.BooleanField(null=True, default=None)
    user_ip = models.CharField(max_length=200, null=True, default=None)
    latitude = models.CharField(max_length=200, null=True, default=None)
    longitude = models.CharField(max_length=200, null=True, default=None)
    datetime_log = models.CharField(max_length=200, null=True, default=None)
    date_updated = models.DateTimeField(null=True, default=None)


class banktransferstatement(models.Model):
    batchid = models.BigAutoField(primary_key=True)
    debitno = models.CharField(max_length=21)
    date = models.CharField(max_length=21)
    narration = models.CharField(max_length=21)
    filename = models.CharField(max_length=21)
    name = models.CharField(max_length=30)
    bank = models.CharField(max_length=40)
    branch = models.CharField(max_length=20)
    ifsc = models.CharField(max_length=20)
    accountno = models.BigIntegerField()
    amount = models.CharField(max_length=30)


class bank_details(models.Model):
    B_Id = models.BigAutoField(primary_key=True)
    holder_name = models.CharField(max_length=150, null=True, default=None)
    bank_name = models.CharField(max_length=150, null=True, default=None)
    acc_no = models.CharField(max_length=50, null=True, default=None)
    branch = models.CharField(max_length=150, null=True, default=None)
    acc_type = models.CharField(max_length=150, null=True, default=None)
    ifsc = models.CharField(max_length=50, null=True, default=None)
    Pan_no = models.CharField(max_length=50, null=True, default=None)
    P_Id = models.ForeignKey(Employee, on_delete=models.CASCADE, db_column='P_Id')


class case(models.Model):
    create_for = models.CharField(max_length=50)
    case_type = models.CharField(max_length=50)
    case_title = models.TextField()
    case_desc = models.TextField()
    case_id = models.BigAutoField(primary_key=True)
    case_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(Employee, on_delete=models.CASCADE, db_column='P_Id', related_name='created_cases')
    case_status = models.CharField(max_length=30, default='New')
    assigned_to = models.ForeignKey(Employee, on_delete=models.CASCADE, db_column='assigned_to', null=True, default=None, related_name='assigned_cases')
    class Meta:
        indexes = [
            models.Index(fields=['created_by'], name='case_created_by_idx'),
            models.Index(fields=['assigned_to'], name='case_assigned_to_idx'),
        ]


class certificate(models.Model):
    id = models.BigAutoField(primary_key=True)
    Email_id = models.CharField(max_length=50)
    en_no = models.CharField(max_length=50)
    course_title = models.CharField(max_length=50)


class chat(models.Model):
    chatid = models.BigAutoField(primary_key=True)
    sender_id = models.CharField(max_length=50)
    reciever_id = models.CharField(max_length=50)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    case_id = models.ForeignKey(case, on_delete=models.CASCADE, db_column='case_id')

    class Meta:
        indexes = [
            models.Index(fields=['case_id'], name='chat_case_id_idx'),
        ]


class chatbot_categories(models.Model):
    cat_id = models.BigAutoField(primary_key=True)
    category = models.CharField(max_length=255)
    c_id = models.IntegerField(null=True, default=None)

    class Meta:
        indexes = [
            models.Index(fields=['c_id'], name='chatbot_categories_c_id_idx'),
        ]
    c_id = models.ForeignKey(Company, on_delete=models.CASCADE, db_column='c_id')


class chatbot_questions(models.Model):
    id = models.BigAutoField(primary_key=True)
    category_id = models.BigIntegerField()
    question = models.CharField(max_length=255)
    reply = models.CharField(max_length=255)
    class Meta:
        indexes = [
            models.Index(fields=['category_id'], name='chatbot_questions_category'),
        ]
    category_id = models.ForeignKey('chatbot_categories', on_delete=models.CASCADE, db_column='category_id')



class clearance(models.Model):
    Clearance_Id = models.BigAutoField(primary_key=True)
    Accounts = models.CharField(max_length=5, default='No')
    Hr = models.CharField(max_length=5, default='No')
    Hr_Plant = models.CharField(max_length=5, default='No')
    IT = models.CharField(max_length=5, default='No')
    Project = models.CharField(max_length=5, default='No')
    status = models.CharField(max_length=20, default='Pending')
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE, db_column='P_Id', related_name='clearances_requested')
    given_by = models.ForeignKey(Employee, on_delete=models.CASCADE, db_column='given_by', null=True, default=None, related_name='clearances_given')
    class Meta:
        indexes = [
            models.Index(fields=['employee_id'], name='clearance_employee_idx'),
            models.Index(fields=['given_by'], name='clearance_given_by_idx'),
        ]


class comments(models.Model):
    cid = models.BigAutoField(primary_key=True)
    uid = models.CharField(max_length=120, null=True, default=None)
    date = models.TextField(null=True, default=None)
    message = models.TextField(null=True, default=None)
    vid = models.CharField(max_length=300)
    course_name = models.CharField(max_length=300, null=True, default=None)
    com = models.CharField(max_length=3000)

class course(models.Model):
    course_id = models.BigAutoField(primary_key=True)
    course_title = models.CharField(max_length=25)
    description = models.CharField(max_length=500)
    Thumbnail = models.CharField(max_length=500)
    c_id = models.IntegerField()
    c_name = models.CharField(max_length=50)

class course_Employee(models.Model):
    id = models.BigAutoField(primary_key=True)
    course_title = models.CharField(max_length=60)
    Email_id = models.CharField(max_length=50)
    status = models.IntegerField()
    Start_date = models.DateTimeField(auto_now_add=True)


class custom_forms(models.Model):
    seq = models.BigAutoField(primary_key=True)
    form_name = models.CharField(max_length=255)
    c_id = models.IntegerField()
    alloc = models.CharField(max_length=250, null=True, default=None)

    class Meta:
        indexes = [
            models.Index(fields=['c_id'], name='custom_forms'),
        ]
    c_id = models.ForeignKey(Company, on_delete=models.CASCADE, db_column='c_id')

class custom_forms_questions(models.Model):
    label = models.CharField(max_length=250)
    type = models.CharField(max_length=20, null=True, default=None)
    ID = models.CharField(max_length=50)
    name = models.CharField(max_length=50, primary_key=True)
    optionName = models.CharField(max_length=250, null=True, default=None)
    form_name = models.CharField(max_length=255)
    c_id = models.IntegerField()

    class Meta:
        indexes = [
            models.Index(fields=['c_id'], name='custom_forms_questions'),
        ]
    c_id = models.ForeignKey(Company, on_delete=models.CASCADE, db_column='c_id')



class custom_letters(models.Model):
    seq = models.BigAutoField(primary_key=True)
    letter_name = models.CharField(max_length=250)
    c_id = models.IntegerField()
    letter_content = models.TextField(null=True, default=None)
    alloc = models.CharField(max_length=250, null=True, default=None)
    class Meta:
        indexes = [
            models.Index(fields=['letter_name', 'c_id'], name='custom_letters_lname_c_id' ),
            models.Index(fields=['c_id'], name='custom_letters_c_id_idx'),
        ]
    c_id = models.ForeignKey(Company, on_delete=models.CASCADE, db_column='c_id')


class dependent(models.Model):
    D_Id = models.BigAutoField(primary_key=True)
    D_name = models.CharField(max_length=150, null=True, blank=True)
    D_gender = models.CharField(max_length=50, null=True, blank=True)
    D_dob = models.DateField(null=True, blank=True)
    D_relation = models.CharField(max_length=100, null=True, blank=True)
    D_desc = models.TextField(null=True, blank=True)
    P_Id = models.CharField(max_length=50)
    class Meta:
        indexes = [
            models.Index(fields=['P_Id']),
        ]
    P_Id = models.ForeignKey('Employee', on_delete=models.CASCADE, db_column='P_Id')


class earnedleave(models.Model):
    emp_emailid = models.CharField(max_length=50, primary_key=True, default='A@gmail.com')
    earnedleave = models.IntegerField()

class email_alert(models.Model):
    alert_id = models.BigAutoField(primary_key=True)
    status = models.IntegerField()
    type = models.CharField(max_length=200, null=True, default=None)
    title = models.TextField(null=True, default=None)
    deadline = models.TextField(null=True, default=None)
    emp_emailid = models.CharField(max_length=100, null=True, default=None)
    c_name = models.CharField(max_length=30, null=True, default=None)
    task_id = models.IntegerField(null=True, default=None)


class endorsement(models.Model):
    e_id = models.BigAutoField(primary_key=True)
    emailid = models.CharField(max_length=50)
    endorse = models.CharField(max_length=1000)
    from_email = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['emailid'], name='endorsement_emailid'),
        ]

class events(models.Model):
    evt_id = models.BigAutoField(primary_key=True)
    evt_type = models.CharField(max_length=20, null=True, default=None)
    evt_start = models.DateField()
    evt_end = models.DateField()
    evt_text = models.TextField()
    evt_color = models.CharField(max_length=7)
    status = models.BooleanField(default=False)
    emp_emailid = models.CharField(max_length=50, null=True, default=None)

class expenses(models.Model):
    expense_id = models.BigAutoField(primary_key=True)
    emp_emailid = models.CharField(max_length=50)
    expense = models.IntegerField()
    expensedate = models.CharField(max_length=15)
    expenseitm = models.CharField(max_length=255)


class family_details(models.Model):
    F_Id = models.BigAutoField(primary_key=True)
    F_name = models.CharField(max_length=200)
    F_gender = models.CharField(max_length=50)
    F_dob = models.DateField()
    F_contact = models.CharField(max_length=15)
    F_mail = models.CharField(max_length=100)
    F_relation = models.CharField(max_length=100)
    F_comment = models.TextField()
    P_Id = models.CharField(max_length=50)

    class Meta:
        indexes = [
            models.Index(fields=['P_Id'], name='family_details_P_Id'),
        ]
    P_Id = models.ForeignKey(Employee, on_delete=models.CASCADE, db_column='P_Id')

class faqs(models.Model):
    faq_id = models.BigAutoField(primary_key=True)
    question = models.CharField(max_length=500)
    answer = models.CharField(max_length=1000, null=True, default=None)
    emp_emailid = models.ForeignKey(Employee, on_delete=models.CASCADE, db_column='emp_emailid', related_name='faqs_created')
    imp = models.BooleanField(default=False)
    c_id = models.ForeignKey(Company, on_delete=models.CASCADE, db_column='c_id', related_name='faqs')
    class Meta:
        indexes = [
            models.Index(fields=['emp_emailid'], name='faqs_emp_emailid'),
            models.Index(fields=['c_id'], name='faqs_c_id'),
        ]

class feedback(models.Model):
    fid = models.BigAutoField(primary_key=True)
    emp_emailid = models.CharField(max_length=50)
    skill = models.CharField(max_length=1000)
    from_email = models.CharField(max_length=30)
    reason = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

class files(models.Model):
    id = models.BigAutoField(primary_key=True)
    file_name = models.CharField(max_length=255, null=True, default=None)
    job_desc_id = models.IntegerField(null=True, default=None)
    sop_id = models.IntegerField(null=True, default=None)


class forms(models.Model):
    form_id = models.BigAutoField(primary_key=True)
    emp_emailid = models.CharField(max_length=15)
    form_type = models.CharField(max_length=50, choices=[('job_description', 'Job Description'), ('kra_table', 'KRA Table'), ('sop', 'SOP'), ('', 'None')], default='')
    form_data = models.CharField(max_length=100, null=True, default=None)
    ratings = models.CharField(max_length=1, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], default='1')
    remark = models.CharField(max_length=50)
    appreciation = models.CharField(max_length=50)
    status = models.BooleanField(default=None)
    date = models.DateField()
    emp_emailid = models.ForeignKey(Employee, on_delete=models.CASCADE, db_column='emp_emailid')

    class Meta:
        indexes = [
            models.Index(fields=['emp_emailid'], name='forms_emp_emailid_idx'),
        ]

class history(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=50)
    eid = models.TextField()
    score = models.IntegerField()
    level = models.IntegerField()
    correct = models.IntegerField()
    wrong = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    timestamp = models.BigIntegerField()
    status = models.CharField(max_length=40)
    score_updated = models.CharField(max_length=10)


class ITDeclaration80c(models.Model):
    id = models.BigAutoField(primary_key=True)
    Emp_id = models.CharField(max_length=50)
    Investment1 = models.CharField(max_length=30, default='Life Insurance Premium')
    Investment1_Amount = models.IntegerField(default=0)
    Investment2 = models.CharField(max_length=30, default='Public Provident Fund')
    Investment2_Amount = models.IntegerField(default=0)
    Investment3 = models.CharField(max_length=30, default='Unit-Linked Insurance Plan')
    Investment3_Amount = models.IntegerField(default=0)
    Investment4 = models.CharField(max_length=30, default='National Savings Certificates')
    Investment4_Amount = models.IntegerField(default=0)
    Investment5 = models.CharField(max_length=30, default='Mutual Funds')
    Investment5_Amount = models.IntegerField(default=0)
    Investment6 = models.CharField(max_length=30, default='Tution Fees')
    Investment6_Amount = models.IntegerField(default=0)
    class Meta:
        indexes = [
            models.Index(fields=['Emp_id'], name='EmpID_to_Empemail'),
        ]


class itdeclaration80d_new(models.Model):
    Emp_id = models.CharField(max_length=50, primary_key=True)
    Investment1 = models.CharField(max_length=100, default='Medi claim Policy for Self,Spouse,Children-80D')
    Investment1_Amount = models.IntegerField(default=0)
    Investment2 = models.CharField(max_length=100, default='Medi claim Policy for Self,Spouse,Children for senior citizen-80D')
    Investment2_Amount = models.IntegerField(default=0)
    Investment3 = models.CharField(max_length=100, default='Medi claim Policy for Parents-80D')
    Investment3_Amount = models.IntegerField(default=0)
    Investment4 = models.CharField(max_length=100, default='Medi claim Policy or Medical Bills for parents for senior citizen-80D')
    Investment4_Amount = models.IntegerField(default=0)
    Investment5 = models.CharField(max_length=100, default='Preventive health check up - 80D')
    Investment5_Amount = models.IntegerField(default=0)
    Investment6 = models.CharField(max_length=100, default='Preventive health check up for parents - 80D')
    Investment6_Amount = models.IntegerField(default=0)
    Emp_id = models.ForeignKey(Employee, on_delete=models.CASCADE, db_column='Emp_id')

    class Meta:
        indexes = [
            models.Index(fields=['Emp_id'], name='itdeclaration80d_new_Emp_id'),
        ]

class itdeclaration_oie_new(models.Model):
    Emp_id = models.CharField(max_length=50, primary_key=True)
    Investment1 = models.CharField(max_length=50, default='Additional Exemptions on voluntary NPS')
    Investment1_Amount = models.IntegerField(default=0)
    Investment2 = models.CharField(max_length=50, default='Rajiv Gandhi Equity savings scheme')
    Investment2_Amount = models.IntegerField(default=0)
    Investment3 = models.CharField(max_length=50, default='Treatment of dependent with disability')
    Investment3_Amount = models.IntegerField(default=0)
    Investment4 = models.CharField(max_length=50, default='Treatment of dependent with severe disability')
    Investment4_Amount = models.IntegerField(default=0)
    Emp_id = models.ForeignKey(Employee, on_delete=models.CASCADE, db_column='Emp_id')

    class Meta:
        indexes = [
            models.Index(fields=['Emp_id'], name='itdeclaration_oie_new_Emp_id'),
        ]


class itdeclaration_osi_new(models.Model):
    Emp_id = models.CharField(max_length=50, primary_key=True)
    Investment1 = models.CharField(max_length=50, default='Income from other sources')
    Investment1_Amount = models.IntegerField()
    Investment2 = models.CharField(max_length=50, default='Interest Earned from Savings Deposit')
    Investment2_Amount = models.IntegerField()
    Investment3 = models.CharField(max_length=50, default='Interest Earned from Fixed Deposit')
    Investment3_Amount = models.IntegerField()
    Investment4 = models.CharField(max_length=50, default='Interest Earned from National Savings certificates')
    Investment4_Amount = models.IntegerField()
    Emp_id = models.ForeignKey(Employee, on_delete=models.CASCADE, db_column='Emp_id')


class jd_table(models.Model):
    jd_id = models.BigAutoField(primary_key=True)


class job_desc(models.Model):
    job_desc_id = models.BigAutoField(primary_key=True)
    jd_name = models.CharField(max_length=150, null=True, default=None)
    responsiblities = models.CharField(max_length=5000)
    sdate = models.DateField(null=True, default=None)
    ratings = models.IntegerField(default=0)
    selfratings = models.IntegerField(default=0)
    remarks = models.CharField(max_length=50, null=True, default=None)
    status = models.IntegerField(default=0)
    email_id = models.CharField(max_length=100)
    jid = models.IntegerField()


class job_info(models.Model):
     J_Id = models.BigAutoField(primary_key=True)
     job_title = models.CharField(max_length=250, null=True, default=None)
     department = models.CharField(max_length=150, null=True, default=None)
     working_type = models.CharField(max_length=100, null=True, default=None)
     start_date = models.DateField(null=True, default=None)
     P_Id = models.ForeignKey(Employee, on_delete=models.CASCADE, db_column='P_Id')

     class Meta:
         indexes = [
             models.Index(fields=['P_Id'], name='job_info_P_Id_idx'),
         ]

class kra_table(models.Model):
    kra_id = models.BigAutoField(primary_key=True)


class kra(models.Model):
    kra_no = models.BigAutoField(primary_key=True)
    KRA = models.CharField(max_length=50)
    Weightage = models.IntegerField()
    KPI = models.CharField(max_length=500)
    Target = models.CharField(max_length=500)
    ratingsscale = models.CharField(max_length=500)
    RATINGS_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
    ]
    ratings = models.IntegerField(choices=RATINGS_CHOICES)
    selfratings = models.IntegerField(default=0)
    remarks = models.CharField(max_length=500, null=True, default=None)
    status = models.IntegerField(default=0)
    kra_id = models.IntegerField()
    email_id = models.CharField(max_length=100, null=True, default=None)
    kra_id = models.ForeignKey(kra_table, on_delete=models.CASCADE, db_column='kra_id')

    class Meta:
        indexes = [
            models.Index(fields=['kra_id'], name='kra_kra_id_idx'),
        ]

class leavecounttemp(models.Model):
    emp_emailid = models.CharField(max_length=50, primary_key=True, default='A@gmail.com')
    casualleave = models.IntegerField(default=15)
    medicalleave = models.IntegerField(default=15)
    lopleave = models.IntegerField(default=365)
    earnedleave = models.IntegerField()


class leavetype(models.Model):
    id = models.AutoField(primary_key=True)
    LeaveType = models.CharField(max_length=200, null=True)
    Description = models.TextField(null=True)
    Limit = models.IntegerField(default=0)
    CreationDate = models.DateTimeField(auto_now_add=True)

class leave_encashment(models.Model):
    LE_id = models.BigAutoField(primary_key=True)
    txndt = models.DateField()
    refn = models.IntegerField()
    effdt = models.DateField()
    emp = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    blnc = models.IntegerField()
    pdays = models.IntegerField()
    sal = models.IntegerField(null=True)
    enclve = models.IntegerField(null=True)

    class Meta:
        indexes = [
            models.Index(fields=['emp'], name='leave_encashment_emp_idx'),
        ]
class licence(models.Model):
    Licence_Id = models.BigAutoField(primary_key=True)
    licence_no = models.CharField(max_length=100)
    issue_date = models.DateField()
    expiry_date = models.DateField()
    P_Id = models.CharField(max_length=50)
    class Meta:
        indexes = [
            models.Index(fields=['P_Id']),
        ]
    P_Id = models.ForeignKey(Employee, on_delete=models.CASCADE, db_column='P_Id')

class loan(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    emp_emailid = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    lamt = models.IntegerField()
    mamt = models.IntegerField()
    startdate = models.DateField()
    reason = models.CharField(max_length=255)
    status = models.IntegerField()


class login(models.Model):
    login_id = models.BigAutoField(primary_key=True)
    emp_emailid = models.CharField(max_length=50)
    class Meta:
        indexes = [
            models.Index(fields=['emp_emailid'], name='login_emp_emailid_idx'),
        ]
    emp_emailid = models.ForeignKey(Employee, on_delete=models.CASCADE, db_column='emp_emailid')

class messages(models.Model):
    id = models.BigAutoField(primary_key=True)
    message = models.TextField(null=True)
    created_at = models.DateTimeField(null=True)

class off_cycle(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=20)
    tname = models.CharField(max_length=20)
    amt = models.IntegerField()
    effdt = models.DateField()
    note = models.CharField(max_length=255)

class options(models.Model):
    id = models.BigAutoField(primary_key=True)
    qid = models.CharField(max_length=50)
    option = models.CharField(max_length=2000)
    optionid = models.TextField()


class options_static(models.Model):
    id = models.BigAutoField(primary_key=True)
    qid = models.CharField(max_length=50)
    option = models.CharField(max_length=100)
    optionid = models.CharField(max_length=50)


class ot(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    hours_worked = models.IntegerField()
    hourly_rate = models.IntegerField()
    overtime = models.IntegerField()


class pan(models.Model):
    Pan_Id = models.BigAutoField(primary_key=True)
    pan_no = models.BigIntegerField()
    pan_name = models.CharField(max_length=200)
    pan_pic = models.CharField(max_length=150)
    P_Id = models.CharField(max_length=50)
    class Meta:
        indexes = [
            models.Index(fields=['P_Id']),
        ]
    P_Id = models.ForeignKey(Employee, on_delete=models.CASCADE, db_column='P_Id')


class passport(models.Model):
    Pass_Id = models.BigAutoField(primary_key=True)
    passport_no = models.BigIntegerField()
    passport_name = models.CharField(max_length=200)
    passport_validity = models.DateField()
    passport_pic = models.CharField(max_length=150)
    P_Id = models.CharField(max_length=50)
    class Meta:
        indexes = [
            models.Index(fields=['P_Id']),
        ]
    P_Id = models.ForeignKey('Employee', on_delete=models.CASCADE, db_column='P_Id')


class pdf(models.Model):
    pdf_id = models.BigAutoField(primary_key=True)
    pdf_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    course_id = models.IntegerField()
    descr = models.CharField(max_length=100)

class personal_details(models.Model):
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    Contact = models.CharField(max_length=20, null=True, blank=True)
    emergency_name = models.CharField(max_length=60, null=True, blank=True)
    emergency_contact = models.CharField(max_length=60, null=True, blank=True)
    mail = models.CharField(max_length=50 , primary_key=True)
    gender = models.CharField(max_length=20, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    district = models.CharField(max_length=100, null=True, blank=True)
    post_code = models.CharField(max_length=10, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    edit = models.CharField(max_length=10, default='enable')
    class Meta:
        indexes = [
            models.Index(fields=['mail']),
        ]
    mail = models.ForeignKey('Employee', on_delete=models.CASCADE, db_column='emp_emailid')


class poifiles_new(models.Model):
    id = models.BigAutoField(primary_key=True)
    Emp_id = models.CharField(max_length=50)
    Year = models.CharField(max_length=7)
    Investment_1 = models.CharField(max_length=10, default='80C')
    actualAmount_80C = models.IntegerField()
    Doc_80C = models.CharField(max_length=255)
    Status1 = models.CharField(max_length=20, default='Pending')
    Investment_2 = models.CharField(max_length=4, default='80D')
    actualAmount_80D = models.IntegerField()
    Doc_80D = models.CharField(max_length=255)
    Status2 = models.CharField(max_length=20, default='Pending')
    Investment_3 = models.CharField(max_length=4, default='OIE')
    OIE_actualAmount = models.IntegerField()
    OIE_Doc = models.CharField(max_length=255)
    Status3 = models.CharField(max_length=20, default='Pending')
    Investment_4 = models.CharField(max_length=4, default='OSI')
    OSI_actualAmount = models.IntegerField()
    OSI_Doc = models.CharField(max_length=255)
    Status4 = models.CharField(max_length=20, default='Pending')
    class Meta:
        indexes = [
            models.Index(fields=['Emp_id']),
        ]
    Emp_id = models.ForeignKey('Employee', on_delete=models.CASCADE, db_column='emp_emailid')


class qualification(models.Model):
    Q_Id = models.BigAutoField(primary_key=True)
    q_type = models.CharField(max_length=100)
    q_degree = models.CharField(max_length=100)
    q_clg = models.TextField()
    q_uni = models.TextField()
    q_duration = models.IntegerField()
    q_yop = models.IntegerField()
    q_comment = models.TextField(null=True, blank=True)
    P_Id = models.CharField(max_length=50)
    class Meta:
        indexes = [
            models.Index(fields=['P_Id']),
        ]
    P_Id = models.ForeignKey('Employee', on_delete=models.CASCADE, db_column='emp_emailid')

class questions(models.Model):
    id = models.IntegerField(primary_key=True)
    eid = models.TextField()
    qid = models.TextField()
    qns = models.TextField()
    choice = models.IntegerField()
    sn = models.IntegerField()

class questions_static(models.Model):
    id = models.IntegerField(primary_key=True)
    vid = models.CharField(max_length=100)
    qid = models.CharField(max_length=100)
    qns = models.CharField(max_length=5000)
    choice = models.IntegerField()
    sn = models.IntegerField()

class quiz(models.Model):
    id = models.IntegerField(primary_key=True)
    eid = models.TextField()
    title = models.CharField(max_length=100)
    course_title = models.CharField(max_length=100)
    correct = models.IntegerField()
    wrong = models.IntegerField()
    passing = models.IntegerField()
    total = models.IntegerField()
    time = models.BigIntegerField()
    date = models.TextField()
    status = models.CharField(max_length=10)

class reporting(models.Model):
    id = models.IntegerField(primary_key=True)
    c_id = models.IntegerField()
    Reporting_from = models.CharField(max_length=50)
    Reporting_to = models.CharField(max_length=50)

class resignation(models.Model):
    R_Id = models.BigAutoField(primary_key=True)
    submit_date = models.DateTimeField(auto_now_add=True)
    exp_leave = models.DateField()
    notice_per = models.IntegerField(default=30)
    leave_reason = models.TextField()
    leave_reason_2 = models.TextField(null=True, blank=True)
    leave_reason_3 = models.TextField(null=True, blank=True)
    leave_date = models.DateField(null=True, blank=True)
    notice_serve = models.IntegerField()
    settle_date = models.DateField(null=True, blank=True)
    shortfall_date = models.IntegerField(null=True, blank=True)
    exit_interview = models.DateField(null=True, blank=True)
    last_working = models.DateField(null=True, blank=True)
    P_Id = models.CharField(max_length=50)
    status = models.CharField(max_length=30, default='Pending')
    approved_by = models.CharField(max_length=50, null=True, blank=True)
    class Meta:
        indexes = [
            models.Index(fields=['P_Id']),
        ]
    P_Id = models.ForeignKey('Employee', on_delete=models.CASCADE, db_column='emp_emailid')

class resp_47feedback_test(models.Model):
    emp_name = models.CharField(max_length=255, primary_key=True)


class resp_47gh(models.Model):
    emp_name = models.CharField(max_length=255,primary_key=True)

class resp_59Employee_detail_form(models.Model):
    emp_name = models.CharField(max_length=255,primary_key=True)

class resp_59feedback_form(models.Model):
    emp_name = models.CharField(max_length=255,primary_key=True)
    q1 = models.CharField(max_length=255, null=True, blank=True)

class resp_59feedback_form1(models.Model):
    emp_name = models.CharField(max_length=255, primary_key=True)
    q2 = models.CharField(max_length=255, null=True, blank=True)


class resp_60feedback_form(models.Model):
    emp_name = models.CharField(max_length=255, primary_key=True)
    hay = models.CharField(max_length=255, null=True, blank=True)


class resp_148feedback_form(models.Model):
    emp_name = models.CharField(max_length=255, primary_key=True)

class resp_148testt365g(models.Model):
    emp_name = models.CharField(max_length=255, primary_key=True)

class resp_157example_form(models.Model):
    emp_name = models.CharField(max_length=255, primary_key=True)

class resp_157feedback_form(models.Model):
    emp_name = models.CharField(max_length=255, primary_key=True)

class resp_Employee_detail_form(models.Model):
    emp_name = models.CharField(max_length=255,primary_key=True)

class salary(models.Model):
    sal_id = models.IntegerField(primary_key=True)
    id = models.CharField(max_length=50)
    payout_month = models.CharField(max_length=50)
    effective_from = models.CharField(max_length=50, null=True, blank=True)
    revision = models.IntegerField(null=True, blank=True)
    basic = models.FloatField()
    hra = models.FloatField()
    conveyance = models.FloatField()
    da = models.FloatField()
    special_allowance = models.FloatField()
    monthly_ctc = models.FloatField()
    annual_ctc = models.FloatField()
    Eligible_Deductions = models.FloatField()
    Yearly_Taxable_Salary = models.FloatField()
    Total_Tax_Liability = models.FloatField()
    Monthly_TDS = models.FloatField()
    Monthly_EPF = models.FloatField()
    Monthly_Professional_Tax = models.FloatField()
    Net_Salary = models.FloatField()
    paymentmethod = models.CharField(max_length=50, default='Bank')
    notes = models.CharField(max_length=50)
    remarks = models.CharField(max_length=50)
    holdsalary = models.IntegerField(default=0)
    paid = models.IntegerField(default=0)

class score_final(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=50)
    score = models.IntegerField()
    time = models.DateTimeField(auto_now=True)

class sop(models.Model):
    sop_id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=20, null=True, blank=True)
    s_name = models.CharField(max_length=30)
    sdate = models.DateField(null=True, blank=True)
    d_id = models.IntegerField()
    class Meta:
        indexes = [
            models.Index(fields=['d_id']),
        ]
    d_id = models.ForeignKey('Department', on_delete=models.CASCADE, db_column='d_id')


class tasks(models.Model):
    task_id = models.BigAutoField(primary_key=True)
    dpt_head = models.CharField(max_length=50, null=True, blank=True)
    dpt_auditor = models.CharField(max_length=50, null=True, blank=True)
    job_desc_id = models.IntegerField(null=True, blank=True)
    kra_id = models.IntegerField(null=True, blank=True)
    sop_id = models.IntegerField(null=True, blank=True)
    emp_emailid = models.CharField(max_length=50, null=True, blank=True)
    d_id = models.IntegerField(null=True, blank=True)
    status = models.BooleanField(default=False)
    sdate = models.DateField(null=True, blank=True)
    edate = models.DateTimeField(null=True, blank=True)
    tid = models.IntegerField(null=True, blank=True)
    imp = models.BooleanField(default=False)
    selfratings = models.IntegerField(default=0)
    ratings = models.IntegerField(default=0)
    remark = models.CharField(max_length=30, null=True, blank=True)
    class Meta:
        db_table = 'tasks'
        indexes = [
            models.Index(fields=['d_id']),
            models.Index(fields=['dpt_head']),
            models.Index(fields=['dpt_auditor']),
            models.Index(fields=['emp_emailid']),
            models.Index(fields=['job_desc_id']),
            models.Index(fields=['kra_id']),
            models.Index(fields=['sop_id']),
            models.Index(fields=['tid']),
        ]
    d_id = models.ForeignKey('Department', on_delete=models.CASCADE, db_column='d_id', related_name='tasks')
    dpt_head = models.ForeignKey('Employee', on_delete=models.CASCADE, db_column='dpt_head', related_name='tasks_dpt_head')
    dpt_auditor = models.ForeignKey('Employee', on_delete=models.CASCADE, db_column='dpt_auditor', related_name='tasks_dpt_auditor')
    emp_emailid = models.ForeignKey('Employee', on_delete=models.SET_NULL, null=True, blank=True, db_column='emp_emailid', related_name='tasks_emp_emailid')
    job_desc_id = models.ForeignKey('job_desc', on_delete=models.CASCADE, db_column='job_desc_id', null=True, blank=True, related_name='tasks_job_desc')
    kra_id = models.ForeignKey('kra_table', on_delete=models.CASCADE, db_column='kra_id', null=True, blank=True, related_name='tasks_kra')
    sop_id = models.ForeignKey('sop', on_delete=models.CASCADE, db_column='sop_id', null=True, blank=True, related_name='tasks_sop')
    tid = models.ForeignKey('todotasks', on_delete=models.CASCADE, db_column='tid', null=True, blank=True, related_name='tasks_tid')

class tblleaves(models.Model):
    id = models.BigAutoField(primary_key=True)
    LeaveType = models.CharField(max_length=110)
    ToDate = models.CharField(max_length=120)
    FromDate = models.CharField(max_length=120)
    Days = models.IntegerField()
    Description = models.CharField(max_length=500)
    PostingDate = models.DateTimeField(auto_now_add=True)
    AdminRemark = models.CharField(max_length=500, null=True, blank=True)
    AdminRemarkDate = models.CharField(max_length=120, null=True, blank=True)
    Status = models.IntegerField()
    IsRead = models.IntegerField()

class todotasks(models.Model):
    tid = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=300)
    date = models.DateTimeField(auto_now_add=True)
    evt = models.ForeignKey('events', on_delete=models.CASCADE, db_column='evt_id', null=True, blank=True)
    class Meta:
        indexes = [
            models.Index(fields=['evt_id']),
        ]

class user_answer(models.Model):
    id = models.BigAutoField(primary_key=True)
    qid = models.CharField(max_length=50)
    ans = models.CharField(max_length=50)
    correctans = models.CharField(max_length=50)
    eid = models.CharField(max_length=50)
    username = models.CharField(max_length=50)

class video(models.Model):
    video_id = models.BigAutoField(primary_key=True)
    video_name = models.CharField(max_length=100)
    location = models.TextField()
    course_id = models.IntegerField()
    descr = models.CharField(max_length=200)

    class Meta:
        indexes = [
            models.Index(fields=['course_id']),
        ]

class work_exp(models.Model):
    W_Id = models.BigAutoField(primary_key=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    comp_name = models.CharField(max_length=150, null=True, blank=True)
    comp_location = models.CharField(max_length=250, null=True, blank=True)
    designation = models.CharField(max_length=150, null=True, blank=True)
    gross_salary = models.FloatField(null=True, blank=True)
    leave_reason = models.TextField(null=True, blank=True)
    P_Id = models.CharField(max_length=50)
    class Meta:
        indexes = [
            models.Index(fields=['P_Id']),
        ]
    P_Id = models.ForeignKey('Employee', on_delete=models.CASCADE, db_column='emp_emailid')

