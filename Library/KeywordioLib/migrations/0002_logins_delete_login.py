# Generated by Django 4.1.1 on 2022-09-25 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KeywordioLib', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='logins',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('useremail', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='login',
        ),
    ]
