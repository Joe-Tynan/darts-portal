# Generated by Django 5.0.7 on 2024-07-26 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_remove_customuser_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='does_karting',
        ),
    ]