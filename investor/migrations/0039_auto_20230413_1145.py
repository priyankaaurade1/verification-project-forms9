# Generated by Django 3.2.7 on 2023-04-13 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investor', '0038_alter_investorcreditcard_document_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='investorcreditcard',
            name='cc_type',
            field=models.CharField(blank=True, choices=[('VISA', 'VISA'), ('Amex', 'Amex'), ('Other', 'Other'), ('Master Card', 'Master Card')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='investorbankdetail',
            name='account_type',
            field=models.CharField(blank=True, choices=[('NRO', 'NRO'), ('CURRENT', 'CURRENT'), ('NRE', 'NRE'), ('SAVING', 'SAVING')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='investordetail',
            name='martial_status',
            field=models.CharField(blank=True, choices=[('SINGLE', 'SINGLE'), ('MARRIED', 'MARRIED'), ('WIDOWED', 'WIDOWED'), ('DIVORCED', 'DIVORCED'), ('SEPARATED', 'SEPARATED')], max_length=64, null=True),
        ),
    ]
