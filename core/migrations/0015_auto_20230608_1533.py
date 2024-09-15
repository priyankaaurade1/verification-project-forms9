# Generated by Django 3.2.7 on 2023-06-08 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_chooseinvestorfields_investordocumentmanagerfields'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvestorMartialStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='InvestorMartialManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('martial_status', models.CharField(max_length=60)),
                ('documents', models.ManyToManyField(to='core.InvestorMartialStatus')),
            ],
        ),
        migrations.AddField(
            model_name='chooseinvestorfields',
            name='investorMartialManagerFields',
            field=models.ManyToManyField(to='core.InvestorMartialManager'),
        ),
    ]
