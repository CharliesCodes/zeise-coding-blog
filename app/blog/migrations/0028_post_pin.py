# Generated by Django 4.0.2 on 2022-03-09 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0027_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='pin',
            field=models.BooleanField(default=False),
        ),
    ]