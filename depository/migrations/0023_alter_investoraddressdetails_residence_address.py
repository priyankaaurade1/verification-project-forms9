# Generated by Django 3.2.7 on 2023-05-10 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('depository', '0022_auto_20230504_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investoraddressdetails',
            name='residence_address',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
