# Generated by Django 3.1.4 on 2020-12-31 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_auto_20201230_1137'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='announcement',
            options={'get_latest_by': 'pub_date'},
        ),
    ]
