# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_auto_20151207_2040'),
    ]

    operations = [
        migrations.CreateModel(
            name='Papelaria',
            fields=[
                ('entidadeexibicao_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='base.EntidadeExibicao')),
            ],
            options={
                'verbose_name': 'Papelaria',
                'verbose_name_plural': 'Papelaria',
            },
            bases=('base.entidadeexibicao',),
        ),
        migrations.AlterField(
            model_name='destaque',
            name='link',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
