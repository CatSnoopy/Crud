# Generated by Django 5.0.6 on 2024-05-27 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0006_alter_ciudad_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ciudad',
            options={'verbose_name': 'ciudad'},
        ),
        migrations.AlterField(
            model_name='personas',
            name='ciudad',
            field=models.CharField(max_length=100),
        ),
    ]
