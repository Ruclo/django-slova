# Generated by Django 4.0.2 on 2022-02-17 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slovicka', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='odpoved',
            name='spravne',
            field=models.CharField(default='default', max_length=100),
        ),
    ]
