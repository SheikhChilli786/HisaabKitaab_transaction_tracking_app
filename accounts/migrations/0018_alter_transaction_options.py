# Generated by Django 5.0.4 on 2024-06-04 20:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_alter_party_balance'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transaction',
            options={'permissions': (('can_manage_transactions', 'Can Manage Transactions'), ('can_manage_sales', 'Can Manage Sales'), ('can_manage_purchase', 'Can Manage Purchase'), ('can_manage_s/p', 'Can Manage Sale/Purchase'))},
        ),
    ]
