# Generated by Django 4.1.3 on 2023-04-09 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Orphanage', '0002_rename_weblink_orphanage_details_o_weblink'),
    ]

    operations = [
        migrations.AddField(
            model_name='orphanage_details',
            name='username',
            field=models.CharField(default='dhruv', max_length=150, unique=True),
        ),
    ]