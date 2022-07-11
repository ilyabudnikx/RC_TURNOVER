# Generated by Django 4.0.5 on 2022-07-02 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_rc', '0003_category_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_user', models.CharField(max_length=200)),
                ('to_user', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('text_message', models.CharField(max_length=500)),
            ],
        ),
    ]