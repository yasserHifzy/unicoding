# Generated by Django 4.0.6 on 2022-07-23 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0003_account_extra_alter_account_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='extra',
            field=models.JSONField(default=dict, null=True),
        ),
    ]
