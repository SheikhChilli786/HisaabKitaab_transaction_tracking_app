# Generated by Django 5.0.4 on 2024-06-06 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_alter_transaction_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='tradeitem',
            name='delete_flag',
            field=models.IntegerField(default=0),
        ),
    ]