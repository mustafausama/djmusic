# Generated by Django 4.1.2 on 2022-10-07 01:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0004_alter_album_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 7, 1, 50, 42, 401556, tzinfo=datetime.timezone.utc)),
        ),
    ]