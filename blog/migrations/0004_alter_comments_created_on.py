# Generated by Django 4.0.6 on 2022-08-01 20:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_comments_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 1, 20, 28, 58, 738097, tzinfo=utc)),
        ),
    ]
