# Generated by Django 4.0.6 on 2022-07-31 01:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subacount', '0006_alter_journalentery_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journalentery',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='journal_enter', to='subacount.account'),
        ),
    ]
