# Generated by Django 5.1.6 on 2025-02-26 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mozilla', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
    ]
