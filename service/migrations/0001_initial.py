# Generated by Django 4.1.5 on 2023-04-15 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_icon', models.CharField(max_length=20)),
                ('service_title', models.CharField(max_length=50)),
                ('service_desc', models.TextField()),
            ],
        ),
    ]