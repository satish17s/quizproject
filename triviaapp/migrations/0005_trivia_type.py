# Generated by Django 3.1.1 on 2020-09-15 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('triviaapp', '0004_auto_20200915_1223'),
    ]

    operations = [
        migrations.AddField(
            model_name='trivia',
            name='type',
            field=models.IntegerField(choices=[(1, 'Single'), (2, 'Multiple')], default=1),
        ),
    ]