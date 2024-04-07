# Generated by Django 4.0.6 on 2024-04-06 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='category_client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('date_creation', models.DateField()),
                ('date_update', models.DateField()),
                ('satate', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'CategoriaCliente',
            },
        ),
        migrations.AlterField(
            model_name='modelo',
            name='codigo',
            field=models.CharField(max_length=10, unique=True, verbose_name='Código'),
        ),
        migrations.AlterField(
            model_name='modelo',
            name='descripcion',
            field=models.CharField(max_length=50, verbose_name='Descripción'),
        ),
    ]
