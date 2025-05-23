# Generated by Django 4.2.21 on 2025-05-13 16:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets_and_owners_app', '0006_bird'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(50)])),
                ('name', models.CharField(max_length=255)),
                ('vaccinated', models.BooleanField(default='Unknown')),
                ('description', models.TextField(blank=True, default='No description')),
                ('breed', models.TextField(blank='True', default='Unknown')),
            ],
        ),
    ]
