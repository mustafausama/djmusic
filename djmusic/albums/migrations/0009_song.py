# Generated by Django 4.1.2 on 2022-10-28 08:56

import albums.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0008_remove_album_created_at_album_created_album_modified'),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='song_images')),
                ('audio', models.FileField(upload_to='song_audio', validators=[albums.validators.validate_audio_file_extension])),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='albums.album')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
