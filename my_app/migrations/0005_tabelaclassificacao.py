# Generated by Django 4.0.4 on 2022-04-22 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0004_user_bairro_user_numero_da_casa_user_rua'),
    ]

    operations = [
        migrations.CreateModel(
            name='TabelaClassificacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pontos', models.IntegerField()),
                ('quantidade_de_partidas', models.IntegerField()),
                ('quantidade_de_vitorias', models.IntegerField()),
                ('quantidade_de_empates', models.IntegerField()),
                ('quantidade_de_derrotas', models.IntegerField()),
                ('gols_feitos', models.IntegerField()),
                ('gols_sofridos', models.IntegerField()),
                ('nome_do_time', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.equipe', unique=True)),
            ],
        ),
    ]
