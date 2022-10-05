# Generated by Django 4.0.5 on 2022-09-30 18:04

from django.db import migrations, models
import property.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Realtor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('description', models.TextField(blank=True)),
                ('email', models.EmailField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=200, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=property.models.upload_to, verbose_name='Image')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to=property.models.upload_to, verbose_name='Image')),
                ('rooms', models.IntegerField(default=0)),
                ('bathroom', models.IntegerField(default=0)),
                ('parking_spot', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('For Sale', 'For Sale'), ('For Rent', 'For Rent')], default='For Sale', max_length=200, null=True)),
                ('location', models.TextField(blank=True)),
                ('price', models.CharField(max_length=200, null=True)),
                ('photo_1', models.ImageField(blank=True, null=True, upload_to=property.models.upload_to, verbose_name='Image')),
                ('photo_2', models.ImageField(blank=True, null=True, upload_to=property.models.upload_to, verbose_name='Image')),
                ('photo_3', models.ImageField(blank=True, null=True, upload_to=property.models.upload_to, verbose_name='Image')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('realtor', models.ManyToManyField(related_name='agent', to='property.realtor')),
            ],
        ),
    ]
