# Generated by Django 4.2.7 on 2023-12-02 19:28

import django.core.validators
from django.db import migrations, models
import django.utils.timezone
import hitcount.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=200)),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('post_picture', models.ImageField(default='', upload_to='media/')),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('draft', 'draft'), ('published', 'published')], default='draft', max_length=10)),
            ],
            options={
                'ordering': ['-created_time'],
            },
            bases=(hitcount.models.HitCountMixin, models.Model),
        ),
        migrations.CreateModel(
            name='PostAuthor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='PostReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('review', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['-created_time'],
            },
        ),
    ]