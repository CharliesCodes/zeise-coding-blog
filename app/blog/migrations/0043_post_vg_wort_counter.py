# Generated by Django 4.0.6 on 2022-08-19 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0042_post_description_post_header_image_alt_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="vg_wort_counter",
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
