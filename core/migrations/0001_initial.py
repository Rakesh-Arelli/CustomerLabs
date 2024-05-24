# Generated by Django 4.1.4 on 2024-05-23 13:52

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('account_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('account_name', models.CharField(max_length=255)),
                ('app_secret_token', models.CharField(default=uuid.uuid4, editable=False, max_length=255, unique=True)),
                ('website', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('http_method', models.CharField(max_length=10)),
                ('headers', models.JSONField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destinations', to='core.account')),
            ],
        ),
    ]