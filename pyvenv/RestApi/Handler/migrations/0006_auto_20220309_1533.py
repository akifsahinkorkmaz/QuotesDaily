# Generated by Django 3.2.12 on 2022-03-09 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Handler', '0005_auto_20220307_2336'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='printable',
            field=models.CharField(default=16, max_length=400, verbose_name='printable-quote'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='quote',
            name='qfont',
            field=models.IntegerField(default=16, verbose_name='quote-font'),
        ),
        migrations.AlterField(
            model_name='quote',
            name='quote',
            field=models.CharField(max_length=300, verbose_name='quote'),
        ),
    ]
