# Generated by Django 2.2.6 on 2020-01-25 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sankalp_collection', '0005_auto_20200122_2354'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='color',
            field=models.TextField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='articles',
            name='price',
            field=models.CharField(max_length=50),
        ),
    ]
