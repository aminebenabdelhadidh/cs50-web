# Generated by Django 4.1.3 on 2022-12-02 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_bids_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bids',
            name='listin',
        ),
        migrations.AddField(
            model_name='listing',
            name='bid',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='list', to='auctions.bids'),
        ),
    ]
