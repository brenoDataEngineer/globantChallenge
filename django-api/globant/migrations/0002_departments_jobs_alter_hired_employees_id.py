# Generated by Django 4.2.3 on 2023-07-26 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('globant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='departments',
            fields=[
                ('id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('department', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='jobs',
            fields=[
                ('id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('job', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='hired_employees',
            name='id',
            field=models.CharField(max_length=5, primary_key=True, serialize=False),
        ),
    ]
