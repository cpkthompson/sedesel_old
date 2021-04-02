# Generated by Django 2.2.18 on 2021-04-02 20:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('home', '0014_settings'),
    ]

    operations = [
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.URLField(help_text='Your Facebook page URL')),
                ('instagram', models.CharField(help_text='Your Instagram username, without the @', max_length=255)),
                ('youtube', models.URLField(help_text='Your YouTube channel or user account URL')),
                ('favicon', models.FileField(help_text='https://www.favicon-generator.org/', upload_to='favicon/')),
                ('primary_color', models.CharField(blank=True, max_length=15)),
                ('secondary_color', models.CharField(blank=True, max_length=15)),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE,
                                              to='wagtailcore.Site')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Settings',
        ),
    ]