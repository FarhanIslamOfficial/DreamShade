# Generated by Django 4.0 on 2021-12-19 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery_app', '0003_alter_picture_album'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album',
            options={'ordering': ['-created']},
        ),
    ]
