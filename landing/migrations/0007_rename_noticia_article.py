# Generated by Django 5.1.1 on 2024-11-02 23:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0006_alter_noticia_conteudo'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Noticia',
            new_name='Article',
        ),
    ]