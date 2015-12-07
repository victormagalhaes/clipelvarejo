# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_auto_20151203_2213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entidadeexibicao',
            name='preco',
        ),
        migrations.AddField(
            model_name='destaque',
            name='link',
            field=models.CharField(default=b'', max_length=200),
        ),
    ]
