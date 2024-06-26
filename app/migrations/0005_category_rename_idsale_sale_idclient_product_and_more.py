# Generated by Django 4.0.6 on 2024-04-06 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_sale'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('date_creation', models.DateField()),
                ('date_update', models.DateField()),
                ('state', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Categoria',
            },
        ),
        migrations.RenameField(
            model_name='sale',
            old_name='idsale',
            new_name='idclient',
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('priceiva', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('status_iva', models.BooleanField(default=True)),
                ('state', models.BooleanField(default=True)),
                ('idcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.category')),
            ],
            options={
                'verbose_name_plural': 'Producto',
            },
        ),
        migrations.CreateModel(
            name='DetailSale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idproducto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
                ('idsale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.sale')),
            ],
        ),
    ]
