# Generated by Django 2.2.3 on 2019-07-13 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ai_talks', '0003_speaker_sort'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScientificCommittee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('position', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='StaticParts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.TextField()),
                ('register_link', models.CharField(max_length=1000)),
            ],
        ),
    ]
