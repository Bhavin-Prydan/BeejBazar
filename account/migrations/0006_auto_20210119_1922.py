# Generated by Django 2.2.8 on 2021-01-19 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20210119_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='User_mo',
            field=models.CharField(max_length=11),
        ),
    ]
