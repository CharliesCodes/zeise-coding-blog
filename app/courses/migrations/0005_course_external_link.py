# Generated by Django 4.0.6 on 2022-08-28 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_delete_courselist'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='external_link',
            field=models.URLField(default=None, null=True),
        ),
    ]
