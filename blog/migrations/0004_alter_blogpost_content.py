# Generated by Django 4.2.15 on 2024-10-07 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blogpost_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='content',
            field=models.TextField(),
        ),
    ]