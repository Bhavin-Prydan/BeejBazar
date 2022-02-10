# Generated by Django 2.2.8 on 2021-03-03 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0013_order_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_us',
            fields=[
                ('contact_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=48)),
                ('contact_no', models.BigIntegerField()),
                ('desc', models.TextField()),
            ],
        ),
    ]