# Generated by Django 4.0.5 on 2022-10-08 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0006_remove_listing_realtor_listing_realtor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='realtor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='agent', to='property.realtor'),
        ),
    ]
