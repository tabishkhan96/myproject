# Generated by Django 3.0.8 on 2021-08-17 05:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mymodel',
            old_name='matrial',
            new_name='material',
        ),
    ]
