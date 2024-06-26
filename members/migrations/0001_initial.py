# Generated by Django 5.0.6 on 2024-05-28 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25, verbose_name='書名')),
                ('isbn', models.CharField(max_length=13, unique=True, verbose_name='ISBN')),
                ('author_lname', models.CharField(max_length=5, verbose_name='姓')),
                ('author_fname', models.CharField(max_length=20, verbose_name='名')),
                ('publisher', models.CharField(max_length=20, verbose_name='出版社')),
            ],
        ),
    ]
