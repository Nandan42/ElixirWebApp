# Generated by Django 3.0.2 on 2020-04-14 08:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_admin', '0011_auto_20200414_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='level_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user_admin.module_level'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='module_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user_admin.program_module'),
        ),
    ]
