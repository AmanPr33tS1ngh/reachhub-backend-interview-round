# Generated by Django 5.0.4 on 2024-04-21 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('level', models.CharField(choices=[('ERROR', 'Error'), ('INFO', 'Info')], max_length=5)),
                ('message', models.TextField()),
                ('userId', models.IntegerField(max_length=20)),
            ],
        ),
    ]