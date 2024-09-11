from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.apps import apps

@receiver(post_migrate)
def create_default_leave_types(sender, **kwargs):
    if sender.name == 'happyPerformerBackend':  # Ensure it only runs for your specific app
        Leavetype = apps.get_model('happyPerformerBackend', 'Leavetype')
        Company = apps.get_model('happyPerformerBackend', 'Company')

        # Fetch the first available company; modify as necessary if you have specific company logic
        company = Company.objects.first()
        
        if company:
            # Define the desired leave types dynamically in a list of dictionaries
            leave_types = [
                {'LeaveType': 'Casual Leave', 'Description': 'Casual Leave Description', 'Limit': 15},
                {'LeaveType': 'Medical Leave', 'Description': 'Medical Leave Description', 'Limit': 15},
                {'LeaveType': 'Earned Leave', 'Description': 'Earned Leave Description', 'Limit': 20},
                {'LeaveType': 'LOP Leave', 'Description': 'LOP Leave Description', 'Limit': 20},
            ]

            # Iterate over each leave type and add it if it does not exist
            for leave in leave_types:
                leavetype_obj, created = Leavetype.objects.get_or_create(
                    LeaveType=leave['LeaveType'],
                    company=company,
                    defaults={
                        'Description': leave['Description'],
                        'Limit': leave['Limit'],
                    }
                )
                if created:
                    print(f"Leave type '{leave['LeaveType']}' created.")
                else:
                    print(f"Leave type '{leave['LeaveType']}' already exists.")