# Generated by Django 2.2.3 on 2019-07-28 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20190728_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
