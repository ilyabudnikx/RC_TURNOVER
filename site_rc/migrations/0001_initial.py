# Generated by Django 4.0.5 on 2022-07-01 17:08

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=21)),
                ('password', models.CharField(max_length=128)),
                ('number_phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('real_name', models.CharField(max_length=30)),
                ('avatar', models.ImageField(upload_to='avatar')),
                ('rating', models.IntegerField()),
                ('country_id', models.IntegerField()),
                ('city_id', models.IntegerField()),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('online', models.BooleanField()),
            ],
        ),
    ]