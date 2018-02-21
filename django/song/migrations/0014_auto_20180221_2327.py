# Generated by Django 2.0.2 on 2018-02-21 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0013_song_song_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='lyrics',
            field=models.TextField(blank=True, verbose_name='가사'),
        ),
        migrations.AlterField(
            model_name='song',
            name='title',
            field=models.CharField(max_length=100, verbose_name='곡 제목'),
        ),
    ]