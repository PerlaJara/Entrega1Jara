# Generated by Django 4.1.1 on 2022-09-23 02:38

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0002_alter_post_contenido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='comentario',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
