# Generated by Django 3.2 on 2022-03-09 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cross_word', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horizonalhint',
            name='crossword_id',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='verticalhint',
            name='crossword_id',
            field=models.IntegerField(default=0),
        ),
    ]