# Generated by Django 4.0.4 on 2022-06-02 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_estudiantes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Materias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('camada', models.IntegerField()),
                ('fecha_de_inicio', models.DateField()),
            ],
        ),
    ]
