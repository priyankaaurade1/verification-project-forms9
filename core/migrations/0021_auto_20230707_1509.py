# Generated by Django 3.2.7 on 2023-07-07 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_auto_20230706_1508'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvestorMaritalManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marital', models.CharField(blank=True, max_length=20)),
                ('documentss', models.ManyToManyField(to='core.InvestorSelectDocument')),
            ],
        ),
        migrations.AddField(
            model_name='chooseinvestorfields',
            name='investorMaritalManagerFields',
            field=models.ManyToManyField(to='core.InvestorMaritalManager'),
        ),
    ]
