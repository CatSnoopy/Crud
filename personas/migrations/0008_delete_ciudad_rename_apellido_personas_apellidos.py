# Generated by Django 5.0.6 on 2024-05-30 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0007_alter_ciudad_options_alter_personas_ciudad'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ciudad',
        ),
        migrations.RenameField(
            model_name='personas',
            old_name='apellido',
            new_name='apellidos',
        ),
    ]