# Generated by Django 2.1.5 on 2019-06-19 04:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20190619_1116'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Defenses',
            new_name='Defense',
        ),
        migrations.RenameModel(
            old_name='Passings',
            new_name='Passing',
        ),
        migrations.RenameModel(
            old_name='Receivings',
            new_name='Receiving',
        ),
        migrations.RenameModel(
            old_name='Rushings',
            new_name='Rushing',
        ),
    ]
