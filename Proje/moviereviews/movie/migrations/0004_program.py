# Generated by Django 4.1.3 on 2022-11-14 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_uyelik'),
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=350)),
            ],
        ),
    ]