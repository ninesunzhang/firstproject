# Generated by Django 3.0.8 on 2020-07-21 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('pub_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'books',
            },
        ),
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('gender', models.BooleanField(default=True)),
                ('content', models.CharField(max_length=20)),
                ('Book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookApp.Book')),
            ],
        ),
    ]
