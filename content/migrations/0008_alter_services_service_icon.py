# Generated by Django 4.2 on 2024-01-01 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0007_alter_services_service_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='service_icon',
            field=models.FileField(blank=True, null=True, upload_to='Service Icon'),
        ),
    ]
