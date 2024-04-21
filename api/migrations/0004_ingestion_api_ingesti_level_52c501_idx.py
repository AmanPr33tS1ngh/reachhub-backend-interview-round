# Generated by Django 5.0.4 on 2024-04-21 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_ingestion_api_ingesti_level_a1c1d9_idx_and_more'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='ingestion',
            index=models.Index(fields=['level', 'userId'], name='api_ingesti_level_52c501_idx'),
        ),
    ]