# Generated by Django 3.2.12 on 2022-03-09 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Handler', '0007_alter_quote_quote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='printable',
            field=models.TextField(max_length=400, verbose_name='printable-quote'),
        ),
    ]
