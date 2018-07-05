# Generated by Django 2.0.5 on 2018-06-12 14:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friendly_name', models.CharField(max_length=32)),
                ('name_on_card', models.CharField(max_length=128)),
                ('expiry_date', models.DateField(blank=True, null=True)),
                ('typec', models.CharField(max_length=64)),
                ('cvv', models.CharField(max_length=3)),
                ('card_number', models.CharField(max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
