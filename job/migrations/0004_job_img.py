# Generated by Django 3.1.1 on 2020-09-23 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_job_catogery'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='img',
            field=models.ImageField(default=1, upload_to='jobs/'),
            preserve_default=False,
        ),
    ]
