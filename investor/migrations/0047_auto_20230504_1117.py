# Generated by Django 3.2.7 on 2023-05-04 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investor', '0046_auto_20230503_2201'),
    ]

    operations = [
        migrations.AddField(
            model_name='investornomineedetail',
            name='nominee_city',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='investornomineedetail',
            name='nominee_country',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='investornomineedetail',
            name='nominee_declaration_1',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='investornomineedetail',
            name='nominee_declaration_2',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='investornomineedetail',
            name='nominee_mobile_no',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='investornomineedetail',
            name='nominee_pincode',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='investornomineedetail',
            name='nominee_state',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='investornomineedetail',
            name='registration_no',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='investornomineedetail',
            name='title',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='investorbankdetail',
            name='account_type',
            field=models.CharField(blank=True, choices=[('CURRENT', 'CURRENT'), ('NRE', 'NRE'), ('NRO', 'NRO'), ('SAVING', 'SAVING')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='investorcreditcard',
            name='cc_type',
            field=models.CharField(blank=True, choices=[('VISA', 'VISA'), ('Amex', 'Amex'), ('Other', 'Other'), ('Master Card', 'Master Card')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='investornomineedetail',
            name='nominee_aadhar',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='investornomineedetail',
            name='nominee_address',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='investornomineedetail',
            name='nominee_email',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='investornomineedetail',
            name='nominee_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='investornomineedetail',
            name='nominee_nickname',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
