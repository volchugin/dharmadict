# Generated by Django 3.0.8 on 2021-05-02 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_page_shorttitle'),
    ]

    operations = [
        migrations.RenameField(
            model_name='term',
            old_name='sa2en',
            new_name='sa2en1',
        ),
        migrations.RenameField(
            model_name='term',
            old_name='sa2ru',
            new_name='sa2ru1',
        ),
        migrations.AddField(
            model_name='term',
            name='sa2en2',
            field=models.CharField(blank=True, default='', max_length=216),
        ),
        migrations.AddField(
            model_name='term',
            name='sa2en3',
            field=models.CharField(blank=True, default='', max_length=216),
        ),
        migrations.AddField(
            model_name='term',
            name='sa2ru2',
            field=models.CharField(blank=True, default='', max_length=216),
        ),
        migrations.AddField(
            model_name='term',
            name='sa2ru3',
            field=models.CharField(blank=True, default='', max_length=216),
        ),
    ]