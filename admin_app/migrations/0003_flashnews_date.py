# Generated by Django 5.0.1 on 2024-02-22 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0002_flashnews'),
    ]

    operations = [
        migrations.AddField(
            model_name='flashnews',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
