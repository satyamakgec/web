# Generated by Django 2.0.5 on 2018-05-19 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enssubdomain', '0003_enssubdomainregistration_signed_msg'),
    ]

    operations = [
        migrations.AddField(
            model_name='enssubdomainregistration',
            name='txn_hash_3',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
    ]
