# Generated by Django 4.0.1 on 2022-01-31 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store_data', '0004_alter_userweight_options'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='userweight',
            table='user_weight',
        ),
    ]
