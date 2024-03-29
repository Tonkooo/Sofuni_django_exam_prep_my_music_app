# Generated by Django 5.0.2 on 2024-02-22 22:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0001_initial'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='artist_name',
            field=models.CharField(max_length=30, verbose_name='Artist'),
        ),
        migrations.AlterField(
            model_name='album',
            name='image_url',
            field=models.URLField(verbose_name='Image URL'),
        ),
        migrations.AlterField(
            model_name='album',
            name='name',
            field=models.CharField(max_length=30, unique=True, verbose_name='Album Name'),
        ),
        migrations.AlterField(
            model_name='album',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.profile'),
        ),
    ]
