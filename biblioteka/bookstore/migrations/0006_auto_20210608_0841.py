# Generated by Django 3.2.3 on 2021-06-08 06:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0005_feedback'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='year',
            new_name='genre',
        ),
        migrations.CreateModel(
            name='BookReservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.IntegerField(max_length=100)),
                ('genre', models.CharField(max_length=100)),
                ('reservation_date', models.DateTimeField(auto_now=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
