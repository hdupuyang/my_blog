# Generated by Django 2.1.8 on 2019-12-28 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlepost',
            name='pic',
            field=models.ImageField(blank=True, upload_to='pic/%Y%m%d/'),
        ),
    ]