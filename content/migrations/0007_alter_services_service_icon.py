# Generated by Django 4.2 on 2024-01-01 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0006_services'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='service_icon',
            field=models.FileField(null=True, upload_to='Service Icon'),
        ),
    ]
