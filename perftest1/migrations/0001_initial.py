# Generated by Django 3.0.5 on 2020-04-28 14:36

from django.db import migrations, models
import perftest1.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(max_length=100)),
                ('datum_kreiranja', models.DateField(default=perftest1.models.sada)),
                ('datum_vazenja', models.DateField(default=perftest1.models.sada)),
            ],
            options={
                'verbose_name': 'test',
                'verbose_name_plural': 'testovi',
            },
        ),
    ]
