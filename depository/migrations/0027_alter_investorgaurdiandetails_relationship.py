# Generated by Django 3.2.7 on 2023-05-30 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('depository', '0026_auto_20230518_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investorgaurdiandetails',
            name='relationship',
            field=models.CharField(blank=True, choices=[('MOTHER', 'MOTHER'), ('FATHER', 'FATHER'), ('WIFE', 'WIFE'), ('HUSBAND', 'HUSBAND'), ('SISTER', 'SISTER'), ('BROTHER', 'BROTHER'), ('SON', 'SON'), ('DAUGHTER', 'DAUGHTER'), ('OTHER', 'OTHER')], max_length=50, null=True),
        ),
    ]
