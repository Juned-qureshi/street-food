# Generated by Django 5.0.6 on 2024-07-20 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_contact_desc'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='desc',
            new_name='decs',
        ),
    ]
