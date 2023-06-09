# Generated by Django 4.1.3 on 2023-05-02 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Orphanage', '0003_orphanage_details_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orphanage_Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
                ('o_name', models.CharField(max_length=150)),
                ('e_name', models.CharField(max_length=150)),
                ('e_img', models.ImageField(upload_to='pics')),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
            ],
        ),
    ]
