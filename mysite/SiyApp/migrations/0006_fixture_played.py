# Generated by Django 2.1.4 on 2019-02-22 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SiyApp', '0005_player_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='fixture',
            name='played',
            field=models.CharField(default='no', max_length=128),
        ),
    ]