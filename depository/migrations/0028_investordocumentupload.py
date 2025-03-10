# Generated by Django 3.2.7 on 2023-06-06 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('investor', '0065_auto_20230607_0006'),
        ('depository', '0027_alter_investorgaurdiandetails_relationship'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvestorDocumentUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.ManyToManyField(to='investor.Document')),
                ('request_no', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='document_details', to='depository.requestdetails')),
            ],
        ),
    ]
