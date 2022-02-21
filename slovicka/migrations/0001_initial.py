# Generated by Django 4.0.2 on 2022-02-17 18:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cvicenie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazov', models.CharField(max_length=50)),
                ('datum', models.DateTimeField(verbose_name='Datum uverejnenia')),
                ('trieda', models.CharField(choices=[('1.A', '1.A'), ('2.A', '2.A')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Slovicko',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jazyk1', models.CharField(max_length=30)),
                ('jazyk2', models.CharField(max_length=30)),
                ('cvicenie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='slovicka.cvicenie')),
            ],
        ),
        migrations.CreateModel(
            name='Pokus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cvicenie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='slovicka.cvicenie')),
                ('ziak', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Odpoved',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spravne', models.CharField(max_length=100)),
                ('odpoved', models.CharField(max_length=100)),
                ('jespravne', models.BooleanField(default=None)),
                ('pokus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='slovicka.pokus')),
                ('ziak', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]