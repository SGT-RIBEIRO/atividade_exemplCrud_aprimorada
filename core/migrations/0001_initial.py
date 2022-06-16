# Generated by Django 4.0.5 on 2022-06-16 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genero', models.CharField(max_length=100, verbose_name='Gênero')),
            ],
            options={
                'verbose_name': 'Genero',
                'verbose_name_plural': 'Generos',
            },
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=150, verbose_name='Descricao')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Preco')),
                ('quantidade', models.IntegerField(verbose_name='Quantidade')),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.genero')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
            },
        ),
    ]
