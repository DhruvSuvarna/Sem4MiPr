# Generated by Django 4.1.3 on 2023-04-29 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Donor', '0003_servicedonation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicedonation',
            old_name='Service',
            new_name='service',
        ),
    ]