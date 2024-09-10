from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.apps import apps

@receiver(post_migrate)
def create_default_leave_types(sender, **kwargs):
    # Import models inside the function to avoid AppRegistryNotReady exception
    if sender.name == 'happyPerformerBackend':  # Replace with your actual app name
        Leavetype = apps.get_model('happyPerformerBackend', 'Leavetype')  # Replace with your actual app name
        Company = apps.get_model('happyPerformerBackend', 'Company')  # Replace with your actual app name

        # Assuming there's already a company with ID 1; adjust as needed.
        company = Company.objects.first()
        
        if company and Leavetype.objects.count() == 0:  # Check to avoid duplicates
            Leavetype.objects.create(LeaveType='Casual Leave', Description='Casual Leave Description', Limit=15, company=company)
            Leavetype.objects.create(LeaveType='Medical Leave', Description='Medical Leave Description', Limit=15, company=company)
            Leavetype.objects.create(LeaveType='Earned Leave', Description='Earned Leave Description', Limit=20, company=company)
            print("Default leave types created!")
