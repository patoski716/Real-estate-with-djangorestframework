# Generated by Django 4.0.5 on 2022-10-10 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_alter_listing_realtor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='listing',
        ),
    ]