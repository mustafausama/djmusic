# Generated by Django 4.1.2 on 2022-10-13 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0006_alter_album_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
    ]
