# Generated by Django 4.2.2 on 2023-06-26 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=20)),
                ('rsa', models.CharField(max_length=20)),
                ('pfa', models.CharField(max_length=255)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('isActive', models.BooleanField(default=False)),
            ],
        ),
    ]