# Generated by Django 2.2.18 on 2021-04-02 21:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('home', '0015_auto_20210402_2053'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='configuration',
            name='favicon',
        ),
        migrations.AlterField(
            model_name='configuration',
            name='facebook',
            field=models.URLField(blank=True, help_text='Your Facebook page URL'),
        ),
        migrations.AlterField(
            model_name='configuration',
            name='instagram',
            field=models.CharField(blank=True, help_text='Your Instagram username, without the @', max_length=255),
        ),
        migrations.AlterField(
            model_name='configuration',
            name='youtube',
            field=models.URLField(blank=True, help_text='Your YouTube channel or user account URL'),
        ),
        migrations.CreateModel(
            name='Favicon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=140)),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                            related_name='+', to='wagtailimages.Image')),
            ],
        ),
        migrations.AddField(
            model_name='configuration',
            name='favicons',
            field=models.ManyToManyField(blank=True, to='home.Favicon'),
        ),
    ]
