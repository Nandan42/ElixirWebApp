# Generated by Django 3.0.2 on 2020-04-27 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_admin', '0026_auto_20200427_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='center',
            name='batch_check',
            field=models.BooleanField(default=False),
        ),
    ]
