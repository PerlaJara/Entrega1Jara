# Generated by Django 4.1.1 on 2022-09-23 02:59

import ckeditor.fields
import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0003_alter_comentario_comentario'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='media',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='comentario',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='contenido',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]