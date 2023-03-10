# Generated by Django 4.1.4 on 2022-12-19 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='superheroAppearance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=40)),
                ('race', models.CharField(max_length=60)),
                ('height', models.CharField(max_length=60)),
                ('weight', models.CharField(max_length=60)),
                ('eyeColor', models.CharField(max_length=40)),
                ('hairColor', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='superheroBiography',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('fullName', models.CharField(max_length=100)),
                ('alterEgos', models.CharField(max_length=250)),
                ('aliases', models.CharField(max_length=250)),
                ('birthPlace', models.CharField(max_length=100)),
                ('firstAppearance', models.CharField(max_length=250)),
                ('publisher', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='superheroConnections',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('groupAffiliation', models.CharField(max_length=1000)),
                ('relatives', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='superheroImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('small', models.ImageField(upload_to='')),
                ('medium', models.ImageField(upload_to='')),
                ('large', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='superheroPowerstats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('intelligence', models.IntegerField()),
                ('strength', models.IntegerField()),
                ('speed', models.IntegerField()),
                ('durability', models.IntegerField()),
                ('power', models.IntegerField()),
                ('combat', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='superheroWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('occupation', models.CharField(max_length=500)),
                ('base', models.CharField(max_length=250)),
            ],
        ),
    ]
