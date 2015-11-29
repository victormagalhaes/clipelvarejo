# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_servico_imagem'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='destaquesecundario',
            options={'verbose_name': 'Destaque Secund\xe1rio', 'verbose_name_plural': 'Destaques Secund\xe1rios'},
        ),
        migrations.RemoveField(
            model_name='destaquesecundario',
            name='ordem',
        ),
        migrations.AddField(
            model_name='destaque',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 29, 13, 59, 53, 107714, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='destaque',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 29, 14, 0, 3, 941561, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='destaquesecundario',
            name='ativo',
            field=models.BooleanField(default=False, verbose_name=b'Destaque ativo'),
        ),
        migrations.AddField(
            model_name='entidadeexibicao',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 29, 14, 0, 6, 904603, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entidadeexibicao',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 29, 14, 0, 10, 478468, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(default=datetime.datetime(2015, 11, 29, 14, 0, 17, 642281, tzinfo=utc), upload_to=b'/home/dandaim/projetos/clipelvarejo/media/servicos'),
            preserve_default=False,
        ),
    ]
