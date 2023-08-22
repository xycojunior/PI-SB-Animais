# Generated by Django 4.2.4 on 2023-08-21 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('nome', models.CharField(max_length=50)),
                ('telefone', models.CharField(max_length=13)),
                ('telefone_fixo', models.CharField(blank=True, max_length=12, null=True)),
            ],
        ),
    ]