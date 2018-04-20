# Generated by Django 2.0.4 on 2018-04-20 19:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('licitacao', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contrato',
            name='criado_em',
            field=models.DateField(default=datetime.datetime(2018, 4, 20, 19, 50, 48, 788192, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='modalidade',
            name='criado_em',
            field=models.DateField(default=datetime.datetime(2018, 4, 20, 19, 50, 48, 789876, tzinfo=utc), verbose_name='Data de abertura'),
        ),
        migrations.AlterField(
            model_name='processo',
            name='criado_em',
            field=models.DateField(default=datetime.datetime(2018, 4, 20, 19, 50, 48, 787573, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tipo',
            name='criado_em',
            field=models.DateField(default=datetime.datetime(2018, 4, 20, 19, 50, 48, 786582, tzinfo=utc)),
        ),
    ]