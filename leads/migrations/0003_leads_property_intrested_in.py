# Generated by Django 4.2.6 on 2023-11-10 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0001_initial'),
        ('leads', '0002_leads_business_intrested_in'),
    ]

    operations = [
        migrations.AddField(
            model_name='leads',
            name='property_intrested_in',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='realestate.commercialrealestate'),
        ),
    ]