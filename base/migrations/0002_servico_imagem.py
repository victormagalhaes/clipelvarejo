# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='servico',
            name='imagem',
            field=models.ImageField(default=datetime.datetime(2015, 11, 29, 13, 10, 3, 635731, tzinfo=utc), upload_to=b'/home/dandaim/projetos/clipelvarejo/media/servicos'),
            preserve_default=False,
        ),
    ]
