# Generated by Django 4.2.1 on 2023-06-13 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pinterest_app', '0005_commet'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Commet',
            new_name='Comment',
        ),
    ]
