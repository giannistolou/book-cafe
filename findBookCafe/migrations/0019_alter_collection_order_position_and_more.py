# Generated by Django 4.2.5 on 2024-09-21 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('findBookCafe', '0018_collection_order_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='order_position',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='shop',
            name='order_position',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]