# Generated by Django 3.2.7 on 2023-03-28 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investor', '0013_auto_20230328_1214'),
    ]

    operations = [
        migrations.AddField(
            model_name='investordetail',
            name='landmark',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
