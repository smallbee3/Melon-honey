# Generated by Django 2.0.2 on 2018-02-08 03:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0005_auto_20180208_1059'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='artist',
            new_name='artists',
        ),
    ]
