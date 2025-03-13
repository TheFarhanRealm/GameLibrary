# Generated by Django 5.1.7 on 2025-03-12 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('genre', models.CharField(max_length=100)),
                ('release_date', models.DateField()),
                ('developer', models.CharField(blank=True, max_length=100, null=True)),
                ('platform', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
