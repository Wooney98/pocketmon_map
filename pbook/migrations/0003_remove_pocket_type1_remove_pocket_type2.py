# Generated by Django 4.1.3 on 2022-12-08 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pbook', '0002_remove_pocket_detail_remove_pocket_type_pocket_type1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pocket',
            name='type1',
        ),
        migrations.RemoveField(
            model_name='pocket',
            name='type2',
        ),
    ]
