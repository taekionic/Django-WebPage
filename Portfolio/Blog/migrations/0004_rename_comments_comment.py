# Generated by Django 4.0.4 on 2022-05-30 21:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0003_comments'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comments',
            new_name='Comment',
        ),
    ]
