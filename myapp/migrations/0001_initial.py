# Generated by Django 5.1.1 on 2024-11-08 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('in_stock', models.CharField(max_length=255)),
            ],
        ),
    ]
