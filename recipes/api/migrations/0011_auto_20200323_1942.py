# Generated by Django 3.0.4 on 2020-03-23 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20200322_2258'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingridient',
            old_name='product_id',
            new_name='product',
        ),
    ]
