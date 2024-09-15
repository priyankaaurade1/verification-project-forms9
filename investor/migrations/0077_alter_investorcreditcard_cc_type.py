# Generated by Django 3.2.7 on 2023-07-07 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investor', '0076_auto_20230706_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investorcreditcard',
            name='cc_type',
            field=models.CharField(blank=True, choices=[('Master Card', 'Master Card'), ('Amex', 'Amex'), ('Other', 'Other'), ('VISA', 'VISA')], max_length=20, null=True),
        ),
    ]
