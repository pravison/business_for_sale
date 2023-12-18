# Generated by Django 4.2.6 on 2023-11-10 07:51

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
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CommercialRealEState',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=200)),
                ('asking_price', models.CharField(max_length=150)),
                ('property_name', models.CharField(max_length=200)),
                ('owner', models.TextField(max_length=300)),
                ('total_rooms', models.CharField(max_length=100)),
                ('current_occupied_rooms', models.CharField(max_length=100)),
                ('average_montly_rental_income', models.CharField(max_length=100)),
                ('property_description', models.TextField(blank=True, null=True)),
                ('number_of_workers', models.IntegerField(default=0)),
                ('building_photo', models.ImageField(blank=True, null=True, upload_to='media')),
                ('room_photos_1', models.ImageField(blank=True, null=True, upload_to='media')),
                ('room_photos_2', models.ImageField(blank=True, null=True, upload_to='media')),
                ('room_photos_3', models.ImageField(blank=True, null=True, upload_to='media')),
                ('room_photos_4', models.ImageField(blank=True, null=True, upload_to='media')),
                ('room_photos_5', models.ImageField(blank=True, null=True, upload_to='media')),
                ('room_photos_6', models.ImageField(blank=True, null=True, upload_to='media')),
                ('title_dead_exists', models.BooleanField(default=False)),
                ('property_square_area', models.CharField(blank=True, max_length=100, null=True)),
                ('property_blue_prints', models.BooleanField(default=False)),
                ('constructed_on', models.DateField(blank=True, null=True)),
                ('property_disputes', models.BooleanField(default=False)),
                ('disputes_description', models.TextField(blank=True, null=True)),
                ('repair_needed', models.BooleanField(default=False)),
                ('repair_description', models.TextField(blank=True, null=True)),
                ('country', models.CharField(max_length=150)),
                ('county', models.CharField(max_length=150)),
                ('locationn', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=150)),
                ('featured', models.BooleanField(default=False)),
                ('closed_deal', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='realestate.category')),
                ('listed_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
