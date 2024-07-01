# Generated by Django 5.0.2 on 2024-06-22 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_customuser_does_karting_customuser_plays_darts'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'ordering': ['first_name', 'last_name']},
        ),
        migrations.AddField(
            model_name='customuser',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]