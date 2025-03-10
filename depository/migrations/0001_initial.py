# Generated by Django 3.2.7 on 2023-02-09 18:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='InvestorAdditionalKycDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dp_reference_number', models.CharField(blank=True, max_length=50, null=True)),
                ('dp_id', models.CharField(blank=True, max_length=10, null=True)),
                ('client_id', models.CharField(blank=True, max_length=10, null=True)),
                ('first_holder_name', models.CharField(blank=True, max_length=50, null=True)),
                ('second_holder_name', models.CharField(blank=True, max_length=50, null=True)),
                ('third_holder_name', models.CharField(blank=True, max_length=50, null=True)),
                ('first_holder_pancard', models.CharField(blank=True, max_length=12, null=True)),
                ('second_holder_pancard', models.CharField(blank=True, max_length=12, null=True)),
                ('third_holder_pancard', models.CharField(blank=True, max_length=12, null=True)),
                ('declaration_name', models.CharField(blank=True, max_length=50, null=True)),
                ('declaration', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='InvestorIdentityDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicant_name', models.CharField(blank=True, max_length=150, null=True)),
                ('maiden_name', models.CharField(blank=True, max_length=50, null=True)),
                ('father_spouse_name', models.CharField(blank=True, max_length=50, null=True)),
                ('mother_name', models.CharField(blank=True, max_length=50, null=True)),
                ('gender', models.CharField(blank=True, max_length=30, null=True)),
                ('date_of_birth', models.DateTimeField(blank=True, null=True)),
                ('martial_status', models.CharField(blank=True, choices=[('SINGLE', 'SINGLE'), ('MARRIED', 'MARRIED'), ('WIDOWED', 'WIDOWED'), ('DIVORCED', 'DIVORCED'), ('SEPARATED', 'SEPARATED'), ('OTHER', 'Other')], max_length=30, null=True)),
                ('nationality', models.CharField(blank=True, max_length=64, null=True)),
                ('pan_no', models.CharField(blank=True, max_length=12, null=True)),
                ('aadhar_no', models.CharField(blank=True, max_length=14, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='InvestorNomineeDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nominee_name', models.CharField(blank=True, max_length=100, null=True)),
                ('nominee_address', models.CharField(blank=True, max_length=300, null=True)),
                ('nominee_city', models.CharField(blank=True, max_length=50, null=True)),
                ('nominee_pincode', models.CharField(blank=True, max_length=6, null=True)),
                ('nominee_state', models.CharField(blank=True, max_length=60, null=True)),
                ('nominee_country', models.CharField(blank=True, max_length=60, null=True)),
                ('nominee_mobile_no', models.CharField(blank=True, max_length=12, null=True)),
                ('nominee_email_id', models.CharField(blank=True, max_length=60, null=True)),
                ('nominee_date_of_birth', models.DateTimeField(blank=True, null=True)),
                ('nominee_relationship', models.CharField(blank=True, max_length=50, null=True)),
                ('nominee_declaration_1', models.BooleanField(default=False)),
                ('nominee_declaration_2', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='RequestDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requestno', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='InvestorBankDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(blank=True, max_length=150, null=True)),
                ('branch_address', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('pincode', models.CharField(blank=True, max_length=6, null=True)),
                ('state', models.CharField(blank=True, max_length=60, null=True)),
                ('country', models.CharField(blank=True, max_length=60, null=True)),
                ('account_type', models.CharField(blank=True, max_length=20, null=True)),
                ('micr_number', models.CharField(blank=True, max_length=10, null=True)),
                ('account_no', models.CharField(blank=True, max_length=20, null=True)),
                ('ifsc_number', models.CharField(blank=True, max_length=20, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='InvestorAddressDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('residence_address', models.CharField(blank=True, max_length=300, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('pincode', models.CharField(blank=True, max_length=6, null=True)),
                ('state', models.CharField(blank=True, max_length=60, null=True)),
                ('country', models.CharField(blank=True, max_length=60, null=True)),
                ('mobile_no', models.CharField(blank=True, max_length=12, null=True)),
                ('tel_no', models.CharField(blank=True, max_length=12, null=True)),
                ('email_id', models.CharField(blank=True, max_length=60, null=True)),
                ('permanent_address', models.CharField(blank=True, max_length=300, null=True)),
                ('permanent_city', models.CharField(blank=True, max_length=50, null=True)),
                ('permanent_district', models.CharField(blank=True, max_length=50, null=True)),
                ('permanent_pincode', models.CharField(blank=True, max_length=6, null=True)),
                ('permanent_state', models.CharField(blank=True, max_length=60, null=True)),
                ('permanent_country', models.CharField(blank=True, max_length=60, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
