# Generated by Django 2.0.2 on 2019-12-07 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novel', '0014_auto_20191207_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='link_to',
            field=models.URLField(),
        ),
    ]
