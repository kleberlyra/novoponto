# Generated by Django 5.1.6 on 2025-02-21 03:54

import django.db.models.deletion
import smart_selects.db_fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sisponto', '0003_remove_company_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='state',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sisponto.state', verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='company',
            name='city',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='state', chained_model_field='state', on_delete=django.db.models.deletion.CASCADE, to='sisponto.city', verbose_name='Município'),
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nome')),
                ('sponsor', models.CharField(max_length=255, verbose_name='Responsável pela Unidade')),
                ('address', models.CharField(max_length=255, verbose_name='Endereço')),
                ('neighborhood', models.CharField(max_length=255, verbose_name='Bairro')),
                ('zip_code', models.CharField(max_length=8, verbose_name='CEP')),
                ('phone', models.CharField(max_length=11, verbose_name='Telefone')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('is_active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sisponto.city', verbose_name='Município')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sisponto.company', verbose_name='Empresa')),
            ],
            options={
                'verbose_name': 'Unidade',
                'verbose_name_plural': 'Unidades',
                'ordering': ['company', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nome')),
                ('is_active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sisponto.company', verbose_name='Empresa')),
                ('sector_parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sisponto.sector', verbose_name='Setor Pai')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sisponto.unit', verbose_name='Unidade')),
            ],
            options={
                'verbose_name': 'Setor',
                'verbose_name_plural': 'Setores',
                'ordering': ['company', 'unit', 'name'],
            },
        ),
    ]
