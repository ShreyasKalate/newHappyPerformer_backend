# Generated by Django 5.0.4 on 2024-08-07 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('happyPerformerBackend', '0007_rename_marks_obtained_quiz_total_marks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='emp_phone',
            field=models.CharField(max_length=20),
        ),
    ]
