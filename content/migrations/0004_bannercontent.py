# Generated by Django 4.2.8 on 2023-12-29 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_delete_pricing_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BannerContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner_header_english', models.CharField(max_length=625)),
                ('banner_contnet_english', models.TextField()),
                ('banner_header_arabic', models.CharField(max_length=625)),
                ('banner_contnet_arabic', models.TextField()),
            ],
        ),
    ]
