# Generated by Django 4.0 on 2024-12-02 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='nombre_de_usuario',
            field=models.CharField(db_index=True, max_length=150, unique=True),
        ),
    ]
