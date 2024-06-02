# Generated by Django 5.0.6 on 2024-06-01 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Author',
            new_name='Autor',
        ),
        migrations.RenameModel(
            old_name='Category',
            new_name='Categoria',
        ),
        migrations.RenameField(
            model_name='autor',
            old_name='name',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='categoria',
            old_name='name',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='author',
            new_name='autor',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='category',
            new_name='categoria',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='content',
            new_name='contenido',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='titulo',
        ),
    ]