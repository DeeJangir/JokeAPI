# Generated by Django 2.2.3 on 2019-07-30 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0004_joketext_quotestext'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotestext',
            name='quotes_author',
            field=models.CharField(default='', max_length=140),
        ),
    ]
