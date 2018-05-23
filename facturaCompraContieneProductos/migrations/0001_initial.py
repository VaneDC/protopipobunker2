# Generated by Django 2.0.4 on 2018-05-22 02:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('facturaCompra', '0001_initial'),
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='facturaCompraContieneProductos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.FloatField()),
                ('cantidad', models.IntegerField()),
                ('descuento', models.FloatField()),
                ('idFacturaCompra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facturaCompra.facturaCompra')),
                ('idProducto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='productos.Producto')),
            ],
        ),
    ]
