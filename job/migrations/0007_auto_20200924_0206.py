# Generated by Django 3.1.1 on 2020-09-24 00:06

from django.db import migrations, models
import job.models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0006_job_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='img',
            field=models.ImageField(upload_to=job.models.img_upload),
        ),
    ]
