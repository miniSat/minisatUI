# Generated by Django 2.0 on 2017-12-17 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ram', models.IntegerField()),
                ('cpus', models.IntegerField()),
                ('disk_size', models.IntegerField()),
            ],
        ),
    ]