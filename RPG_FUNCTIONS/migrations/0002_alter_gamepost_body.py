# Generated by Django 5.0.6 on 2024-05-27 13:08

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RPG_FUNCTIONS', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamepost',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
    ]
