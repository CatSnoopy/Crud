# Generated by Django 5.0.6 on 2024-06-04 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0008_delete_ciudad_rename_apellido_personas_apellidos'),
    ]

    operations = [
        migrations.AddField(
            model_name='personas',
            name='viable',
            field=models.CharField(choices=[('viable', 'Viable'), ('No_viable', 'No viable')], default='', max_length=20),
        ),
    ]
