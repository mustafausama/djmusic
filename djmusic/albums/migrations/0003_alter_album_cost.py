# Generated by Django 4.1.2 on 2022-10-07 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0002_alter_album_released_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='cost',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]