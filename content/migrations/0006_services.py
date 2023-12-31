# Generated by Django 4.2 on 2024-01-01 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_remove_contact_us_code_contact_us_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name_english', models.CharField(max_length=50)),
                ('service_name_arabic', models.CharField(max_length=50)),
                ('service_icon', models.FileField(upload_to='Service Icon')),
                ('demo_link', models.URLField()),
            ],
        ),
    ]
