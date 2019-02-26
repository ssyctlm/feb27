# Generated by Django 2.0.7 on 2019-02-21 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=30)),
                ('product_num', models.IntegerField()),
                ('produce_time', models.DateTimeField()),
                ('produce_time1', models.DateField()),
                ('description', models.TextField()),
                ('pictures', models.BooleanField()),
                ('other_content', models.TextField()),
            ],
        ),
    ]
