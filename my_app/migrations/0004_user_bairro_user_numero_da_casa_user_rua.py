# Generated by Django 4.0.4 on 2022-04-22 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0003_remove_equipe_user_fk_user_equipe'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bairro',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='numero_da_casa',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='rua',
            field=models.CharField(default='', max_length=150),
            preserve_default=False,
        ),
    ]
