# Generated by Django 3.0.8 on 2020-07-21 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='admin_friendly_name',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
