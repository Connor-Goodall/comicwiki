# Generated by Django 4.1.4 on 2023-01-03 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comics', '0005_alter_superheroimages_medium'),
    ]

    operations = [
        migrations.AlterField(
            model_name='superheroimages',
            name='medium',
            field=models.ImageField(upload_to='images'),
        ),
    ]