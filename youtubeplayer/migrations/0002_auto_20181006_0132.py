# Generated by Django 2.1 on 2018-10-06 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtubeplayer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ytvideo',
            name='next_url',
            field=models.CharField(default='0', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ytvideo',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
