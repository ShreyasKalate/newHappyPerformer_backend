# Generated by Django 5.0.4 on 2024-09-16 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('happyPerformerBackend', '0015_alter_feedback_emp_emailid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tblleaves',
            name='AdminRemarkDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
