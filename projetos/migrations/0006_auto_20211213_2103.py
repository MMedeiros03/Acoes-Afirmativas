# Generated by Django 3.2.9 on 2021-12-14 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projetos', '0005_alter_projetos_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='projetos',
            name='anexo',
            field=models.FileField(default=1, upload_to='static/anexos/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projetos',
            name='imagem',
            field=models.ImageField(default=0, upload_to='static/imagens/'),
            preserve_default=False,
        ),
    ]
