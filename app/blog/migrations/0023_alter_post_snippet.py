# Generated by Django 4.0.2 on 2022-03-06 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0022_post_snippet"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="snippet",
            field=models.CharField(max_length=200),
        ),
    ]
