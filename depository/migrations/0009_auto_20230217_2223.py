# Generated by Django 3.2.7 on 2023-02-17 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('depository', '0008_auto_20230217_1138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='depository',
            name='is_approved',
        ),
        migrations.RemoveField(
            model_name='depository',
            name='is_completed',
        ),
        migrations.AddField(
            model_name='depository',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='requestdetails',
            name='is_approved',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
