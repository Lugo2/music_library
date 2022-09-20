# Generated by Django 4.1 on 2022-09-20 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MusicLibrary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tile', models.CharField(max_length=250)),
                ('artist', models.CharField(max_length=250)),
                ('album', models.CharField(max_length=400)),
                ('release', models.DateField(max_length=400)),
                ('genre', models.CharField(max_length=400)),
            ],
        ),
    ]