# Generated by Django 3.2.7 on 2023-07-06 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_chooseinvestorfields_investormaritalmanagerfields'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chooseinvestorfields',
            name='investorMaritalManagerFields',
        ),
        migrations.AddField(
            model_name='investordocumentmanager',
            name='marital',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.DeleteModel(
            name='InvestorMaritalManager',
        ),
    ]
