# Generated by Django 4.2.1 on 2023-06-01 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=50)),
                ('number', models.IntegerField()),
            ],
            options={
                'db_table': 'polls',
            },
        ),
    ]
