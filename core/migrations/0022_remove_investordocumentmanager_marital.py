# Generated by Django 3.2.7 on 2023-07-07 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_auto_20230707_1509'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='investordocumentmanager',
            name='marital',
        ),
    ]
