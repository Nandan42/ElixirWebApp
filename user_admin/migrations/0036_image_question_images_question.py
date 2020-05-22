# Generated by Django 3.0.2 on 2020-05-15 07:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_admin', '0035_auto_20200511_1653'),
    ]

    operations = [
        migrations.CreateModel(
            name='images_question',
            fields=[
                ('question_id', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=100, unique=True)),
                ('answer', models.CharField(max_length=500)),
                ('question_type', models.CharField(choices=[('Multiple Image', 'Multiple Image')], max_length=100)),
                ('option1', models.ImageField(default='none.jpg', upload_to='question_image_2')),
                ('option2', models.ImageField(default='none.jpg', upload_to='question_image_2')),
                ('option3', models.ImageField(default='none.jpg', upload_to='question_image_2')),
                ('option4', models.ImageField(default='none.jpg', upload_to='question_image_2')),
                ('comments', models.CharField(blank=True, max_length=500, null=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
                ('level_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_admin.module_level')),
                ('module_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_admin.program_module')),
                ('program_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_admin.program')),
            ],
        ),
        migrations.CreateModel(
            name='image_question',
            fields=[
                ('question_id', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.ImageField(default='none.jpg', upload_to='question_image_1')),
                ('answer', models.CharField(max_length=500)),
                ('question_type', models.CharField(choices=[('Single Image', 'Single Image')], max_length=100)),
                ('comments', models.CharField(blank=True, max_length=500, null=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
                ('level_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_admin.module_level')),
                ('module_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_admin.program_module')),
                ('program_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_admin.program')),
            ],
        ),
    ]
