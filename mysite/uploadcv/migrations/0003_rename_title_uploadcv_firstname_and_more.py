# Generated by Django 4.1.3 on 2022-11-15 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uploadcv', '0002_uploadcv_content_uploadcv_is_published'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uploadcv',
            old_name='title',
            new_name='FirstName',
        ),
        migrations.RenameField(
            model_name='uploadcv',
            old_name='content',
            new_name='LastName',
        ),
    ]
