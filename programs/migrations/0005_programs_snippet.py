# Generated by Django 3.0.8 on 2020-08-19 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0004_auto_20200819_2035'),
    ]

    operations = [
        migrations.AddField(
            model_name='programs',
            name='snippet',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
