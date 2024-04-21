# Generated by Django 5.0.4 on 2024-04-21 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_ingestion_userid'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='ingestion',
            index=models.Index(fields=['level'], name='api_ingesti_level_a1c1d9_idx'),
        ),
        migrations.AddIndex(
            model_name='ingestion',
            index=models.Index(fields=['userId'], name='api_ingesti_userId_aa0b15_idx'),
        ),
    ]
