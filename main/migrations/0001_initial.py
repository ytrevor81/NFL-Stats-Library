# Generated by Django 2.1.5 on 2019-06-18 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.CharField(max_length=45)),
                ('test_two', models.CharField(max_length=100)),
            ],
        ),
    ]
