# Generated by Django 3.2.7 on 2023-03-28 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investor', '0014_investordetail_landmark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investordetail',
            name='landmark',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
