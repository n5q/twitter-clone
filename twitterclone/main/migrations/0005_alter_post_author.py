# Generated by Django 4.2.4 on 2023-08-27 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rename_body_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(default='', max_length=50),
        ),
    ]