# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_auto_20151129_1431'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destaqueprincipal',
            name='is_principal',
        ),
        migrations.AlterField(
            model_name='destaque',
            name='imagem',
            field=models.ImageField(upload_to=b'/Users/victor/projetos/clipelvarejo/media/destaque'),
        ),
        migrations.AlterField(
            model_name='entidadeexibicao',
            name='imagem',
            field=models.ImageField(upload_to=b'/Users/victor/projetos/clipelvarejo/media/servicos'),
        ),
    ]
