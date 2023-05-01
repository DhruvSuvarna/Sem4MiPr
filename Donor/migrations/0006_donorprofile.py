# Generated by Django 4.1.3 on 2023-05-01 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Donor', '0005_alter_servicedonation_mobile'),
    ]

    operations = [
        migrations.CreateModel(
            name='DonorProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='rajat', max_length=150)),
                ('profile_pic', models.ImageField(upload_to='pics')),
                ('mobile', models.BigIntegerField()),
                ('location', models.CharField(max_length=150)),
            ],
        ),
    ]