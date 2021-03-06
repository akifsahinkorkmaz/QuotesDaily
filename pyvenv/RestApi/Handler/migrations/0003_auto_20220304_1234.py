# Generated by Django 3.2.12 on 2022-03-04 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Handler', '0002_auto_20220301_1758'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotebank',
            name='imgtype',
            field=models.CharField(choices=[('1.jpg', 'diamond'), ('2.jpg', 'heart'), ('3.jpg', 'round')], default='1.jpg', max_length=6, verbose_name='bg-image'),
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=20, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='author',
            name='surname',
            field=models.CharField(max_length=20, verbose_name='surname'),
        ),
    ]
