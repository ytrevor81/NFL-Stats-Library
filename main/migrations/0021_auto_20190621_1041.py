# Generated by Django 2.1.5 on 2019-06-21 03:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_auto_20190621_1008'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rushings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=50)),
                ('year', models.CharField(max_length=50)),
                ('team', models.CharField(max_length=100)),
                ('games', models.CharField(max_length=50)),
                ('att', models.CharField(max_length=50)),
                ('att_g', models.CharField(max_length=50)),
                ('yards', models.CharField(max_length=50)),
                ('yards_g', models.CharField(max_length=50)),
                ('yards_c', models.CharField(max_length=50)),
                ('td', models.CharField(max_length=50)),
                ('lng', models.CharField(max_length=50)),
                ('fd', models.CharField(max_length=50)),
                ('rush_twenty_plus', models.CharField(max_length=50)),
                ('rush_forty_plus', models.CharField(max_length=50)),
                ('fum', models.CharField(max_length=50)),
                ('team_short', models.CharField(max_length=50)),
                ('player_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Profiles')),
            ],
        ),
        migrations.RemoveField(
            model_name='rushing',
            name='player_id',
        ),
        migrations.DeleteModel(
            name='Rushing',
        ),
    ]
