# Generated by Django 3.1.4 on 2020-12-30 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='name',
            field=models.CharField(choices=[('C', '客户'), ('CM', '客户经理'), ('S', '客服'), ('SM', '客服经理'), ('F', '冻结用户')], max_length=2, primary_key=True, serialize=False),
        ),
    ]
