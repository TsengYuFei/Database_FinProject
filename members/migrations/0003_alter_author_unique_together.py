# Generated by Django 5.0.6 on 2024-06-05 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_administrator_author_member_publisher_station_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='author',
            unique_together={('fname', 'lname')},
        ),
    ]
