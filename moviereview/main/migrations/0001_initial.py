# Generated by Django 4.2.3 on 2023-07-30 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('director', models.CharField(max_length=300)),
                ('cast', models.CharField(max_length=300)),
                ('release_date', models.DateField()),
                ('description', models.TextField(max_length=5000)),
                ('rating', models.FloatField()),
            ],
        ),
    ]