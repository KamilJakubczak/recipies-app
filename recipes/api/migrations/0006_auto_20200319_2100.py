# Generated by Django 3.0.4 on 2020-03-19 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20200319_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingridient',
            name='grams',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ingridient',
            name='milimiters',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ingridient',
            name='pieces',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]