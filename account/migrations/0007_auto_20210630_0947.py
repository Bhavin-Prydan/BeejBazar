# Generated by Django 2.2.8 on 2021-06-30 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20210119_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='User_mo',
            field=models.BigIntegerField(),
        ),
    ]
