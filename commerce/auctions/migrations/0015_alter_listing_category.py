# Generated by Django 4.1.3 on 2022-12-14 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0014_rename_catg_listing_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(blank=True, default='No category', max_length=64),
        ),
    ]
