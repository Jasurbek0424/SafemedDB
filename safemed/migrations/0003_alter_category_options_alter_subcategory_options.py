# Generated by Django 5.0.3 on 2024-03-06 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('safemed', '0002_alter_product_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='subcategory',
            options={'verbose_name': 'Sub-Category', 'verbose_name_plural': 'Sub-Categories'},
        ),
    ]
