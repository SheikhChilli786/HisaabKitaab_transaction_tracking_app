# Generated by Django 5.0.3 on 2024-04-01 02:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_user_assigned_staff'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': (('can_assign_staff', 'Can Assign Staff to Users'),)},
        ),
    ]
