# Generated by Django 2.0.7 on 2018-08-10 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('threads', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='onepost',
            options={'verbose_name_plural': 'Posts'},
        ),
        migrations.RemoveField(
            model_name='thread',
            name='posts',
        ),
        migrations.AddField(
            model_name='onepost',
            name='number_of_replies',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='onepost',
            name='thread',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='threads.Thread'),
            preserve_default=False,
        ),
    ]
