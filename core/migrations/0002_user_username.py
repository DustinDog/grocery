# Generated by Django 4.2.6 on 2023-11-15 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='def', max_length=60, blank=True, null=True),
        ),
    ]
