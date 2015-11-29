# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20151129_1400'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='imagem',
        ),
        migrations.RemoveField(
            model_name='servico',
            name='imagem',
        ),
        migrations.AddField(
            model_name='entidadeexibicao',
            name='imagem',
            field=models.ImageField(default='a', upload_to=b'/home/dandaim/projetos/clipelvarejo/media/servicos'),
            preserve_default=False,
        ),
    ]
