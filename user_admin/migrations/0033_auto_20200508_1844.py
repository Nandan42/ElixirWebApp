# Generated by Django 3.0.3 on 2020-05-08 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_admin', '0032_delete_student_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='question_type',
            field=models.CharField(choices=[('Multiple Choice', 'Multiple Choice'), ('Fill Ups', 'Fill Ups')], max_length=100),
        ),
    ]
