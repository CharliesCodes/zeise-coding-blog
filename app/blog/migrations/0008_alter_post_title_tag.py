# Generated by Django 4.0.2 on 2022-02-21 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0007_alter_post_title_tag"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="title_tag",
            field=models.CharField(
                default="ZC Blog | TEST", max_length=200, unique=True
            ),
        ),
    ]
