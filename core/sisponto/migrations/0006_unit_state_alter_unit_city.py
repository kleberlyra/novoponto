# Generated by Django 5.1.6 on 2025-02-21 16:49

import django.db.models.deletion
import smart_selects.db_fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sisponto', '0005_alter_company_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='state',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sisponto.state', verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='unit',
            name='city',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='state', chained_model_field='state', on_delete=django.db.models.deletion.CASCADE, to='sisponto.city', verbose_name='Município'),
        ),
    ]
