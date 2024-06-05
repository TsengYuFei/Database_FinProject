# Generated by Django 5.0.6 on 2024-06-05 07:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20, verbose_name='名')),
                ('lname', models.CharField(max_length=5, verbose_name='姓')),
                ('acc', models.CharField(max_length=30, unique=True, verbose_name='帳號')),
                ('passwd', models.CharField(max_length=30, verbose_name='密碼')),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20, verbose_name='名')),
                ('lname', models.CharField(max_length=5, verbose_name='姓')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=10, unique=True, verbose_name='電話')),
                ('ssn', models.CharField(max_length=10, unique=True, verbose_name='身分證')),
                ('fname', models.CharField(max_length=20, verbose_name='名')),
                ('lname', models.CharField(max_length=5, verbose_name='姓')),
                ('sex', models.CharField(choices=[('M', '男性'), ('F', '女性')], max_length=1, null=True, verbose_name='性別')),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='出版社名稱')),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addr', models.CharField(max_length=40, unique=True, verbose_name='地址')),
                ('name', models.CharField(max_length=10, verbose_name='站名')),
                ('statu', models.CharField(choices=[('0', '維修中'), ('1', '營運中')], max_length=1, verbose_name='狀態')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25, verbose_name='書名')),
                ('isbn', models.CharField(max_length=13, unique=True, verbose_name='ISBN')),
                ('img', models.ImageField(null=True, upload_to='book_images/', verbose_name='書本封面')),
                ('statu', models.CharField(choices=[('0', '站內'), ('1', '借出')], default='0', max_length=1, verbose_name='狀態')),
                ('author', models.ManyToManyField(related_name='books', to='members.author', verbose_name='作者')),
                ('member', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='members.member', verbose_name='會員')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='members.publisher', verbose_name='出版社')),
                ('station', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='members.station', verbose_name='站點')),
            ],
        ),
    ]
