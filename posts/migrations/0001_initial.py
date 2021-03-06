# Generated by Django 2.0.6 on 2019-05-17 17:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('title', models.CharField(max_length=200)),
                ('naamdier', models.TextField()),
                ('latijnsenaam', models.TextField()),
                ('uiterlijk', models.TextField()),
                ('kortebeschrijving', models.TextField()),
                ('verspreidingwild', models.TextField()),
                ('geslachtsonderscheid', models.TextField()),
                ('huisvesting', models.TextField()),
                ('inrichting', models.TextField()),
                ('voeding', models.TextField()),
                ('voortplanting', models.TextField()),
                ('draagtijdincubatiegrootbrengen', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('published_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('views', models.IntegerField(default=0)),
                ('tag', models.CharField(blank=True, max_length=30, null=True)),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='posts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
