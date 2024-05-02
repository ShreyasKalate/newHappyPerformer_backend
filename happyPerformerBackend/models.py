from django.db import models

STATUS = {
    '1': 'Active',
    '2': 'Inactive',
}

class Department(models.Model):
    d_id = models.IntegerField(primary_key=True)
    d_name = models.CharField(max_length=30, unique=True)
    add_date = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.d_name
    
class Role(models.Model):
    name = models.CharField(max_length=30, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class Employee(models.Model):
    emp_name = models.CharField(max_length=30)
    emp_emailid = models.EmailField(max_length=250, unique=True, primary_key=True)
    emp_skills = models.CharField(max_length=250)
    emp_pwd = models.CharField(max_length=250)
    emp_phone = models.CharField(max_length=10)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    emp_role = models.ForeignKey(Role, on_delete=models.CASCADE)
    add_date = models.DateField(auto_now=True)
    pay_sts = models.BooleanField(default=False)
    Status = models.CharField(max_length=10, choices = STATUS, default="Active")
    likes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.emp_emailid
