# Generated by Django 4.1.13 on 2024-09-21 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('findBookCafe', '0015_alter_simplepage_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=160)),
                ('slug', models.CharField(max_length=300, unique=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_on', models.DateField(auto_now=True)),
                ('thumbnail', models.ImageField(null=True, upload_to='uploads/')),
                ('shops', models.ManyToManyField(to='findBookCafe.shop')),
            ],
        ),
    ]
