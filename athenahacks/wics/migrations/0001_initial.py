# Generated by Django 2.2 on 2019-04-07 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.TextField(blank=True, default='')),
                ('email', models.TextField(blank=True, default='')),
                ('zip_code', models.TextField(blank=True, default='', max_length=5)),
            ],
        ),
    ]
