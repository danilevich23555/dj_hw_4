# Generated by Django 3.1.2 on 2022-04-06 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_auto_20220405_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='teacher',
            field=models.ManyToManyField(related_name='teacher', to='school.Teacher'),
        ),
    ]