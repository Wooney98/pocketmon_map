# Generated by Django 4.1.3 on 2022-12-08 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pbook', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pocket',
            name='link',
            field=models.CharField(max_length=200),
        ),
    ]
