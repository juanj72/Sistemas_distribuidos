# Generated by Django 3.0.5 on 2021-11-06 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_area', models.CharField(max_length=50)),
                ('descripcion_area', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Estado_tramites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado_tramite', models.CharField(blank=True, max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documento_funci', models.IntegerField()),
                ('nombre_funci', models.CharField(max_length=50)),
                ('apellidos_funci', models.CharField(max_length=50)),
                ('cargo', models.CharField(max_length=50)),
                ('genero_funci', models.CharField(max_length=10)),
                ('passw', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('id_area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.Area')),
            ],
        ),
        migrations.CreateModel(
            name='PPL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nui', models.IntegerField()),
                ('n_td', models.IntegerField()),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('documento', models.IntegerField()),
                ('fecha_nacimiento', models.DateField()),
                ('fecha_captura', models.DateField()),
                ('situacion_juridica', models.CharField(max_length=50)),
                ('genero', models.CharField(max_length=10)),
                ('ubicacion', models.CharField(max_length=50)),
                ('delito', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_tramite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion_tipo', models.CharField(blank=True, max_length=200, null=True)),
                ('nombre_tipo', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('id_area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.Area')),
            ],
        ),
        migrations.CreateModel(
            name='Prestamo_hv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200)),
                ('fecha_prestamo', models.DateField()),
                ('fecha_devolucion', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('id_funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.Funcionario')),
                ('id_ppl', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.PPL')),
            ],
        ),
        migrations.CreateModel(
            name='PPLxTramites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_peticion', models.DateField()),
                ('fase_72h', models.CharField(blank=True, max_length=100, null=True)),
                ('visitadomi_72h', models.CharField(blank=True, max_length=100, null=True)),
                ('antecedentes_72h', models.CharField(blank=True, max_length=100, null=True)),
                ('radi_oficio_libertades', models.IntegerField(blank=True, null=True)),
                ('autoridad_tutela', models.CharField(blank=True, max_length=100, null=True)),
                ('asunto_tutela', models.CharField(blank=True, max_length=100, null=True)),
                ('oficio_envio_tutela', models.CharField(blank=True, max_length=100, null=True)),
                ('observa_desa_tutela', models.CharField(blank=True, max_length=200, null=True)),
                ('observaciones', models.CharField(blank=True, max_length=200, null=True)),
                ('fecha_envio_tramite', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('id_estadotramite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.Estado_tramites')),
                ('id_funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.Funcionario')),
                ('id_ppl', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.PPL')),
                ('id_tipotramite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.Tipo_tramite')),
            ],
        ),
    ]