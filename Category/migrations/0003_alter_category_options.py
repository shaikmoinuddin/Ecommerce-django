# Generated by Django 4.0.5 on 2022-08-13 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Category', '0002_alter_category_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
    ]