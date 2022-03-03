# Generated by Django 3.2.5 on 2021-11-30 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('symbol', models.CharField(max_length=50)),
                ('currentPrice', models.FloatField()),
                ('PreviousPrice', models.FloatField()),
                ('changedPricePercent', models.FloatField()),
            ],
        ),
    ]
