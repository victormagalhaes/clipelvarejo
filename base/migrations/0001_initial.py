# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destaque',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=100)),
                ('subtitulo', models.CharField(max_length=100)),
                ('imagem', models.ImageField(upload_to=b'/home/dandaim/projetos/clipelvarejo/media/destaque')),
            ],
        ),
        migrations.CreateModel(
            name='EntidadeExibicao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=100)),
                ('preco', models.DecimalField(max_digits=7, decimal_places=2)),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='DestaquePrincipal',
            fields=[
                ('destaque_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='base.Destaque')),
                ('is_principal', models.BooleanField(default=False, verbose_name=b'\xc3\x89 destaque principal')),
            ],
            options={
                'verbose_name': 'Destaque Principal',
                'verbose_name_plural': 'Destaques Principais',
            },
            bases=('base.destaque',),
        ),
        migrations.CreateModel(
            name='DestaqueSecundario',
            fields=[
                ('destaque_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='base.Destaque')),
                ('ordem', models.IntegerField()),
            ],
            bases=('base.destaque',),
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('entidadeexibicao_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='base.EntidadeExibicao')),
            ],
            options={
                'verbose_name': 'Presente',
                'verbose_name_plural': 'Presentes',
            },
            bases=('base.entidadeexibicao',),
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('entidadeexibicao_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='base.EntidadeExibicao')),
            ],
            options={
                'verbose_name': 'Servi\xe7o',
                'verbose_name_plural': 'Servi\xe7os',
            },
            bases=('base.entidadeexibicao',),
        ),
    ]
