# Generated by Django 3.1.1 on 2021-10-05 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projetos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projetos',
            name='justificativa',
            field=models.TextField(max_length=2000),
        ),
    ]