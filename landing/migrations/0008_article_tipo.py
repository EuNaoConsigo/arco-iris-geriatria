# Generated by Django 5.1.1 on 2024-11-02 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0007_rename_noticia_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='tipo',
            field=models.CharField(choices=[('noticia', 'Notícias'), ('aviso', 'Avisos'), ('dica', 'Dicas')], default='noticia', max_length=10),
        ),
    ]
