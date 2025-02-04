# Generated by Django 5.0.4 on 2024-06-01 04:34

import happyPerformerBackend.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('happyPerformerBackend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pan',
            name='pan_pic',
            field=models.FileField(default=None, upload_to='PAN/', validators=[happyPerformerBackend.validators.validate_image_extension]),
        ),
        migrations.AlterField(
            model_name='passport',
            name='passport_pic',
            field=models.FileField(default=None, upload_to='Passport/', validators=[happyPerformerBackend.validators.validate_image_extension]),
        ),
    ]
