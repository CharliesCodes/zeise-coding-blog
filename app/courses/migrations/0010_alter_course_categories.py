# Generated by Django 4.0 on 2022-09-13 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0044_alter_post_header_image'),
        ('courses', '0009_rename_discount_course_discount_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='categories',
            field=models.ManyToManyField(related_name='courses', to='blog.Category'),
        ),
    ]
