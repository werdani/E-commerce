# Generated by Django 3.1.7 on 2021-04-03 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='braintree_id',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
