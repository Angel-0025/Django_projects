# Generated by Django 4.1.7 on 2023-05-04 12:12

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DoList',
            new_name='DList',
        ),
        migrations.RenameModel(
            old_name='ToDoList',
            new_name='TDList',
        ),
    ]
