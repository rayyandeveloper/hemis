# Generated by Django 4.2.1 on 2023-05-30 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hemis', '0004_mark_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='mark',
            name='lesson_index',
            field=models.IntegerField(default=0),
        ),
    ]