# Generated by Django 4.2.5 on 2024-01-29 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collegeapp', '0004_category_product_delete_course_delete_department'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='City',
        ),
        migrations.RenameModel(
            old_name='Category',
            new_name='Country',
        ),
    ]