# Generated by Django 4.1.7 on 2023-04-13 14:29

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
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=101)),
                ('text', models.TextField()),
                ('deta_created', models.DateTimeField(auto_now_add=True)),
                ('deta_edited', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('PUB', 'public'), ('DRA', 'draft')], max_length=3)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
