# Generated by Django 3.1.1 on 2020-09-24 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0009_apply_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
