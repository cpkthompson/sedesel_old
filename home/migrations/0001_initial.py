# Generated by Django 2.2.18 on 2021-04-04 15:44

import django.db.models.deletion
import modelcluster.fields
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks
import wagtailstreamforms.blocks
from django.db import migrations, models

import home.models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('wagtailimages', '0001_squashed_0021'),
    ]

    operations = [
        migrations.CreateModel(
            name='CSSClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='FormPage',
            fields=[
                ('page_ptr',
                 models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True,
                                      primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('to_address', models.CharField(blank=True,
                                                help_text='Optional - form submissions will be emailed to these addresses. Separate multiple addresses by comma.',
                                                max_length=255, verbose_name='to address')),
                ('from_address', models.CharField(blank=True, max_length=255, verbose_name='from address')),
                ('subject', models.CharField(blank=True, max_length=255, verbose_name='subject')),
                ('submit_cta', models.CharField(help_text='Example: Submit, Save, Go!', max_length=140)),
                ('thank_you_text', wagtail.core.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='MyFormField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('label',
                 models.CharField(help_text='The label of the form field', max_length=255, verbose_name='label')),
                ('field_type', models.CharField(
                    choices=[('singleline', 'Single line text'), ('multiline', 'Multi-line text'), ('email', 'Email'),
                             ('number', 'Number'), ('url', 'URL'), ('checkbox', 'Checkbox'),
                             ('checkboxes', 'Checkboxes'), ('dropdown', 'Drop down'),
                             ('multiselect', 'Multiple select'), ('radio', 'Radio buttons'), ('date', 'Date'),
                             ('datetime', 'Date/time'), ('hidden', 'Hidden field')], max_length=16,
                    verbose_name='field type')),
                ('required', models.BooleanField(default=True, verbose_name='required')),
                ('choices', models.TextField(blank=True,
                                             help_text='Comma separated list of choices. Only applicable in checkboxes, radio and dropdown.',
                                             verbose_name='choices')),
                ('default_value', models.CharField(blank=True,
                                                   help_text='Default value. Comma separated values supported for checkboxes.',
                                                   max_length=255, verbose_name='default value')),
                ('help_text', models.CharField(blank=True, max_length=255, verbose_name='help text')),
                ('grouping', models.CharField(blank=True, max_length=140)),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StandardPage',
            fields=[
                ('page_ptr',
                 models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True,
                                      primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('introduction', models.TextField(blank=True)),
                ('body', wagtail.core.fields.StreamField([('carousel', wagtail.core.blocks.StructBlock(
                    [('carousel_items', wagtail.core.blocks.ListBlock(home.models.HeroBlock))])), ('hero',
                                                                                                   wagtail.core.blocks.StructBlock(
                                                                                                       [('image',
                                                                                                         wagtail.images.blocks.ImageChooserBlock(
                                                                                                             required=False)),
                                                                                                        ('title',
                                                                                                         wagtail.core.blocks.CharBlock(
                                                                                                             required=True)),
                                                                                                        ('subtitle',
                                                                                                         wagtail.core.blocks.TextBlock(
                                                                                                             required=False)),
                                                                                                        (
                                                                                                        'container_alignment',
                                                                                                        wagtail.core.blocks.ChoiceBlock(
                                                                                                            blank=True,
                                                                                                            choices=[(
                                                                                                                     'w3-display-middle',
                                                                                                                     'Center'),
                                                                                                                     (
                                                                                                                     'w3-display-left container',
                                                                                                                     'Left'),
                                                                                                                     (
                                                                                                                     'w3-display-right container',
                                                                                                                     'Right')])),
                                                                                                        (
                                                                                                        'text_alignment',
                                                                                                        wagtail.core.blocks.ChoiceBlock(
                                                                                                            blank=True,
                                                                                                            choices=[(
                                                                                                                     'w3-center',
                                                                                                                     'Center'),
                                                                                                                     (
                                                                                                                     'w3-left-align',
                                                                                                                     'Left'),
                                                                                                                     (
                                                                                                                     'w3-right-align',
                                                                                                                     'Right')],
                                                                                                            editable=False)),
                                                                                                        ('buttons',
                                                                                                         wagtail.core.blocks.ListBlock(
                                                                                                             home.models.ButtonBlock))])),
                                                          ('introducer', wagtail.core.blocks.StructBlock([('image',
                                                                                                           wagtail.images.blocks.ImageChooserBlock(
                                                                                                               required=False)),
                                                                                                          (
                                                                                                          'image_position',
                                                                                                          wagtail.core.blocks.ChoiceBlock(
                                                                                                              blank=True,
                                                                                                              choices=[(
                                                                                                                       'left',
                                                                                                                       'Left'),
                                                                                                                       (
                                                                                                                       'right',
                                                                                                                       'Right')])),
                                                                                                          ('title',
                                                                                                           wagtail.core.blocks.CharBlock(
                                                                                                               required=True)),
                                                                                                          ('text',
                                                                                                           wagtail.core.blocks.TextBlock(
                                                                                                               max_length=450,
                                                                                                               required=False)),
                                                                                                          ('buttons',
                                                                                                           wagtail.core.blocks.ListBlock(
                                                                                                               home.models.ButtonBlock))])),
                                                          ('grid_of_cards', wagtail.core.blocks.StructBlock(
                                                              [('container_class', wagtail.core.blocks.CharBlock()), (
                                                              'cards',
                                                              wagtail.core.blocks.ListBlock(home.models.CardBlock))])),
                                                          ('padding', wagtail.core.blocks.StructBlock([('size',
                                                                                                        wagtail.core.blocks.IntegerBlock(
                                                                                                            required=True))])),
                                                          ('heading', wagtail.core.blocks.StructBlock(
                                                              [('title', wagtail.core.blocks.CharBlock(required=True)),
                                                               ('size', wagtail.core.blocks.ChoiceBlock(blank=True,
                                                                                                        choices=[('',
                                                                                                                  'Select a header size'),
                                                                                                                 ('h2',
                                                                                                                  'H2'),
                                                                                                                 ('h3',
                                                                                                                  'H3'),
                                                                                                                 ('h4',
                                                                                                                  'H4')],
                                                                                                        required=False)),
                                                               ('subtitle',
                                                                wagtail.core.blocks.CharBlock(required=False))])), (
                                                          'paragraph', wagtail.core.blocks.StructBlock(
                                                              [('text', wagtail.core.blocks.RichTextBlock())])),
                                                          ('embed', wagtail.embeds.blocks.EmbedBlock()), (
                                                          'half_title_text', wagtail.core.blocks.StructBlock([(
                                                                                                              'heading',
                                                                                                              wagtail.core.blocks.StructBlock(
                                                                                                                  [(
                                                                                                                   'title',
                                                                                                                   wagtail.core.blocks.CharBlock(
                                                                                                                       required=True)),
                                                                                                                   (
                                                                                                                   'size',
                                                                                                                   wagtail.core.blocks.ChoiceBlock(
                                                                                                                       blank=True,
                                                                                                                       choices=[
                                                                                                                           (
                                                                                                                           '',
                                                                                                                           'Select a header size'),
                                                                                                                           (
                                                                                                                           'h2',
                                                                                                                           'H2'),
                                                                                                                           (
                                                                                                                           'h3',
                                                                                                                           'H3'),
                                                                                                                           (
                                                                                                                           'h4',
                                                                                                                           'H4')],
                                                                                                                       required=False)),
                                                                                                                   (
                                                                                                                   'subtitle',
                                                                                                                   wagtail.core.blocks.CharBlock(
                                                                                                                       required=False))])),
                                                                                                              (
                                                                                                              'paragraph',
                                                                                                              wagtail.core.blocks.StructBlock(
                                                                                                                  [(
                                                                                                                   'text',
                                                                                                                   wagtail.core.blocks.RichTextBlock())]))])),
                                                          ('form', wagtail.core.blocks.StructBlock(
                                                              [('form', wagtailstreamforms.blocks.FormChooserBlock()), (
                                                              'form_action', wagtail.core.blocks.CharBlock(
                                                                  help_text='The form post action. "" or "." for the current page or a url',
                                                                  required=False)), ('form_reference',
                                                                                     wagtailstreamforms.blocks.InfoBlock(
                                                                                         help_text='This form will be given a unique reference once saved',
                                                                                         required=False))]))],
                                                         blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='Favicon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                            related_name='+', to='wagtailimages.Image')),
            ],
        ),
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_1', models.CharField(blank=True, max_length=140)),
                ('address_2', models.CharField(blank=True, max_length=140)),
                ('city', models.CharField(blank=True, max_length=140)),
                ('country', models.CharField(blank=True, max_length=140)),
                ('facebook', models.URLField(blank=True, help_text='Your Facebook page URL')),
                ('instagram',
                 models.CharField(blank=True, help_text='Your Instagram username, without the @', max_length=255)),
                ('youtube', models.URLField(blank=True, help_text='Your YouTube channel or user account URL')),
                ('primary_color', models.CharField(blank=True, max_length=15)),
                ('secondary_color', models.CharField(blank=True, max_length=15)),
                ('favicons', models.ManyToManyField(blank=True, to='home.Favicon')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE,
                                              to='wagtailcore.Site')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FormField',
            fields=[
                ('myformfield_ptr',
                 models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True,
                                      primary_key=True, serialize=False, to='home.MyFormField')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE,
                                                         related_name='form_fields', to='home.FormPage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=('home.myformfield',),
        ),
    ]
