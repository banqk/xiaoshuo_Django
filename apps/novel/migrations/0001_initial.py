# Generated by Django 2.0.2 on 2019-12-03 16:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import shortuuidfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Novel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('chapters_num', models.IntegerField(default=0)),
                ('words_num', models.IntegerField(default=0)),
                ('profile', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('price', models.FloatField()),
                ('cover_url', models.URLField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'novel',
                'ordering': ['-pub_date'],
            },
        ),
        migrations.CreateModel(
            name='NovelCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'novel_category',
            },
        ),
        migrations.CreateModel(
            name='NovelChapter',
            fields=[
                ('id', shortuuidfield.fields.ShortUUIDField(blank=True, editable=False, max_length=22, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('number', models.IntegerField()),
                ('words_num', models.IntegerField(default=0)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('novel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='novel.Novel')),
            ],
            options={
                'db_table': 'novel_chapter',
            },
        ),
        migrations.CreateModel(
            name='NovelTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='novel.NovelCategory')),
            ],
            options={
                'db_table': 'novel_tag',
            },
        ),
        migrations.AddField(
            model_name='novel',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='novel.NovelCategory'),
        ),
    ]
