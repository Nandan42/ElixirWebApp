# Generated by Django 3.0.2 on 2020-05-21 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_status',
            name='status',
            field=models.CharField(choices=[('S_Pass', 'S_Pass'), ('S_Fail', 'S_Fail'), ('I_Pass', 'I_Pass'), ('I_Fail', 'I_Fail'), ('AV_Pass', 'AV_Pass'), ('AV_Fail', 'AV_Fail'), ('C_Pass', 'C_Pass'), ('C_Fail', 'C_Fail')], max_length=100),
        ),
    ]
