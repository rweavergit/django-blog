# Generated by Django 4.0.2 on 2022-03-07 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0007_post_snippet_alter_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click link above to read more', max_length=255),
        ),
    ]
