# Generated by Django 3.1.4 on 2021-01-05 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0005_auto_20201231_1219'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='announcement',
            options={'get_latest_by': 'pub_date'},
        ),
    ]
