# Generated by Django 3.2.7 on 2023-03-27 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investor', '0010_documentupload_bill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentupload',
            name='bill',
            field=models.CharField(blank=True, choices=[('TELEPHONE_BILL', 'TELEPHONE_BILL'), ('ELECTRIC_BILL', 'ELECTRIC_BILL'), ('UTILITY_BILL', 'UTILITY_BILL'), ('OTHER', 'OTHER')], max_length=64, null=True),
        ),
    ]
