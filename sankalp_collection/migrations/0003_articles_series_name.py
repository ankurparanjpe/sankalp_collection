# Generated by Django 2.2.6 on 2020-01-19 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sankalp_collection', '0002_articleseries'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='series_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='sankalp_collection.ArticleSeries'),
        ),
    ]
