# Generated by Django 4.0.2 on 2022-02-18 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='title', max_length=255),
        ),
    ]
