# Generated by Django 4.0.6 on 2022-08-01 16:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_comments_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
