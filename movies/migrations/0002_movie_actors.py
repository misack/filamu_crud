# Generated by Django 4.2.1 on 2023-05-08 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='actors',
            field=models.TextField(default='Brad Pitt, Margot Robbie, Diego Calva, Jean Smart, Jovan Adepo, and Li Jun Li'),
            preserve_default=False,
        ),
    ]
