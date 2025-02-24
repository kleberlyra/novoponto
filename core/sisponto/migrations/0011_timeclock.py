# Generated by Django 5.1.6 on 2025-02-22 11:44

import django.db.models.deletion
import smart_selects.db_fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sisponto', '0010_person_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeClock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.CharField(max_length=10, verbose_name='Número de Série')),
                ('brand', models.CharField(max_length=255, verbose_name='Marca')),
                ('model', models.CharField(max_length=255, verbose_name='Modelo')),
                ('location', models.CharField(max_length=255, verbose_name='Localização')),
                ('url', models.URLField(verbose_name='URL de Acesso')),
                ('user', models.CharField(max_length=255, verbose_name='Usuário')),
                ('password', models.CharField(max_length=255, verbose_name='Senha')),
                ('is_active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sisponto.company', verbose_name='Empresa')),
                ('unit', smart_selects.db_fields.ChainedForeignKey(chained_field='company', chained_model_field='company', on_delete=django.db.models.deletion.CASCADE, to='sisponto.unit', verbose_name='Unidade')),
            ],
            options={
                'verbose_name': 'Relógio de Ponto',
                'verbose_name_plural': 'Relógios de Ponto',
                'ordering': ['company', 'unit', 'serial_number'],
            },
        ),
    ]
