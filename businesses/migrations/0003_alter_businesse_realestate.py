# Generated by Django 4.2.6 on 2023-11-10 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('businesses', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businesse',
            name='realestate',
            field=models.CharField(choices=[('owned', 'owned'), ('leased', 'leased')], default='leased', max_length=7),
        ),
    ]
