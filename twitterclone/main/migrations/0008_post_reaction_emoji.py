# Generated by Django 4.2.4 on 2023-09-02 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='reaction_emoji',
            field=models.CharField(default='👍', max_length=1),
        ),
    ]
