# Generated by Django 4.1.1 on 2022-09-06 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0003_alter_post_fecha_creacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='fecha_creacion',
            field=models.DateField(editable=False),
        ),
    ]
