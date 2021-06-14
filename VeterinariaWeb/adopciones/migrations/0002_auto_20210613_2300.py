# Generated by Django 3.2.4 on 2021-06-14 03:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adopciones', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='enAdopcion',
            fields=[
                ('idRescatado', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID del animal rescatado dado en adopcion')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('especie', models.CharField(max_length=50, verbose_name='Especie del animal')),
                ('raza', models.CharField(max_length=50, verbose_name='Raza del animal')),
            ],
        ),
        migrations.CreateModel(
            name='EstadoAdopcion',
            fields=[
                ('idCategoria', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID Estado')),
                ('nombreCategoria', models.CharField(max_length=50, verbose_name='Nombre del estado de la adopcion')),
            ],
        ),
        migrations.RemoveField(
            model_name='usuarios',
            name='categoria',
        ),
        migrations.DeleteModel(
            name='TipoUsuario',
        ),
        migrations.DeleteModel(
            name='Usuarios',
        ),
        migrations.AddField(
            model_name='enadopcion',
            name='estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adopciones.estadoadopcion'),
        ),
    ]
