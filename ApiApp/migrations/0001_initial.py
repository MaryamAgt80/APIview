# Generated by Django 4.1.7 on 2023-03-19 10:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('store_name', models.CharField(max_length=100)),
                ('fav', models.BooleanField(default=False)),
                ('description', models.TextField()),
                ('image', models.ImageField(default='', upload_to='image')),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
