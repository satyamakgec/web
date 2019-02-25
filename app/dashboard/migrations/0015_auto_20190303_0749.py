# Generated by Django 2.1.5 on 2019-03-03 07:49

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0014_merge_20190221_2246'),
    ]

    operations = [
        migrations.AddField(
            model_name='bounty',
            name='contract_version',
            field=models.CharField(blank=True, choices=[('1.0', '1.0'), ('1.1', '1.1')], default='1.1', max_length=5),
        ),
        migrations.AlterField(
            model_name='profile',
            name='job_location',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict),
        ),
        migrations.AlterField(
            model_name='tool',
            name='category',
            field=models.CharField(choices=[('AD', 'advanced'), ('TO', 'gas'), ('AL', 'alpha'), ('BA', 'basic'), ('BU', 'tools to build'), ('CS', 'coming soon'), ('CO', 'community'), ('FF', 'just for fun'), ('CR', 'retired')], max_length=2),
        ),
    ]