# Generated by Django 4.2.2 on 2023-06-16 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bankname', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='branch',
            fields=[
                ('ifsc', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('branch', models.CharField(max_length=74)),
                ('address', models.CharField(max_length=195)),
                ('contact', models.IntegerField()),
                ('city', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=26)),
                ('bankname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.bank')),
            ],
        ),
    ]
