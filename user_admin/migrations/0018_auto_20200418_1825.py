# Generated by Django 3.0.2 on 2020-04-18 12:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_admin', '0017_auto_20200418_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='sessions_count',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='batch',
            name='student_count',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='module_level',
            name='level_number',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
