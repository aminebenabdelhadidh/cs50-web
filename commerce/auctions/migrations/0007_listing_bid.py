# Generated by Django 4.1.3 on 2022-12-02 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_rename_listing_bids_listin'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='bid',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='list', to='auctions.bids'),
        ),
    ]
