# Generated by Django 4.0.5 on 2022-06-16 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('nasc', models.CharField(max_length=15)),
                ('rg', models.IntegerField()),
            ],
        ),
    ]
