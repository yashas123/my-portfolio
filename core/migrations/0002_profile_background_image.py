# Generated by Django 3.0.2 on 2020-02-16 15:31

from django.db import migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='background_image',
            field=easy_thumbnails.fields.ThumbnailerImageField(null=True, upload_to='large_profile/'),
        ),
    ]
