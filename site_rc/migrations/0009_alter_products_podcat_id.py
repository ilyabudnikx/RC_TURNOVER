# Generated by Django 4.0.5 on 2022-07-03 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('site_rc', '0008_alter_podcategory_cat_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='podcat_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='site_rc.podcategory'),
        ),
    ]
