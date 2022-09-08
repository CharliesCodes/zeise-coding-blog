# Generated by Django 4.0.6 on 2022-08-18 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0041_rename_picture_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="description",
            field=models.CharField(blank=True, max_length=155),
        ),
        migrations.AddField(
            model_name="post",
            name="header_image_alt",
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name="post",
            name="snippet",
            field=models.CharField(blank=True, default=None, max_length=200),
        ),
    ]