# Generated by Django 2.2.8 on 2021-03-08 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialmedia', '0003_auto_20210306_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(default='default.png', upload_to=''),
        ),
    ]
