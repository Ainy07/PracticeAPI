# Generated by Django 4.1.7 on 2023-04-06 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mission_title', models.CharField(max_length=300)),
                ('mission_completed', models.BooleanField()),
            ],
        ),
    ]
