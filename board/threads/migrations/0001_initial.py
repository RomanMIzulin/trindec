# Generated by Django 2.0.7 on 2018-07-25 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OnePost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_post', models.IntegerField()),
                ('text', models.CharField(max_length=2048)),
                ('published_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_thread', models.IntegerField(verbose_name='Which is this thread?')),
                ('number_of_OnePost', models.IntegerField()),
                ('published_date', models.DateField()),
                ('posts', models.ManyToManyField(to='threads.OnePost')),
            ],
        ),
    ]
