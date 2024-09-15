# Generated by Django 3.2.7 on 2023-03-16 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('depository', '0019_auto_20230226_1303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='investoridentitydetails',
            name='applicant_name',
        ),
        migrations.RemoveField(
            model_name='investoridentitydetails',
            name='father_spouse_name',
        ),
        migrations.RemoveField(
            model_name='investoridentitydetails',
            name='mother_name',
        ),
        migrations.AddField(
            model_name='investoridentitydetails',
            name='applicant_first_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='investoridentitydetails',
            name='applicant_last_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='investoridentitydetails',
            name='applicant_middle_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='investoridentitydetails',
            name='father_first_name',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='investoridentitydetails',
            name='father_last_name',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='investoridentitydetails',
            name='father_middle_name',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='investoridentitydetails',
            name='mother_first_name',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='investoridentitydetails',
            name='mother_last_name',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='investoridentitydetails',
            name='mother_middle_name',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='investoridentitydetails',
            name='residence_address',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='investoridentitydetails',
            name='spouse_first_name',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='investoridentitydetails',
            name='spouse_last_name',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='investoridentitydetails',
            name='spouse_middle_name',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]
