# Generated by Django 4.0.2 on 2022-03-10 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0034_alter_profile_bio_alter_profile_snippet'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
