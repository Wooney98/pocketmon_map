# Generated by Django 4.1.3 on 2022-12-07 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pocket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_url', models.URLField()),
                ('name', models.TextField(max_length=10)),
                ('type', models.TextField(max_length=10)),
                ('height', models.CharField(max_length=10)),
                ('weight', models.CharField(max_length=10)),
                ('classify', models.TextField(max_length=10)),
                ('character', models.TextField(max_length=50)),
                ('detail', models.TextField(max_length=50)),
            ],
        ),
    ]