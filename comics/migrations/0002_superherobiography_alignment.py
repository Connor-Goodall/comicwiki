# Generated by Django 4.1.4 on 2022-12-20 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comics', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='superherobiography',
            name='alignment',
            field=models.CharField(default='neutral', max_length=50),
        ),
    ]