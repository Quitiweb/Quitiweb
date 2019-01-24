# Generated by Django 2.1.1 on 2018-11-08 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qwsite', '0005_auto_20181108_1501'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='education',
            options={'ordering': ('year',), 'verbose_name_plural': 'Education'},
        ),
        migrations.AlterModelOptions(
            name='experience',
            options={'ordering': ('date',), 'verbose_name_plural': 'Experience'},
        ),
        migrations.AlterModelOptions(
            name='training',
            options={'ordering': ('year', 'month'), 'verbose_name_plural': 'Training'},
        ),
        migrations.AlterField(
            model_name='training',
            name='month',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)], default=11, verbose_name='month'),
        ),
    ]