# Generated by Django 3.2.3 on 2021-06-09 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0006_auto_20210608_0841'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='pdf',
        ),
        migrations.AddField(
            model_name='user',
            name='is_user',
            field=models.BooleanField(default=False),
        ),
    ]
