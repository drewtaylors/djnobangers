# Generated by Django 2.1 on 2018-10-08 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtubeplayer', '0002_auto_20181006_0132'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]