# Generated by Django 5.0.6 on 2024-05-22 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trackit', '0002_expensecategory_amount_expensecategory_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expensecategory',
            name='name',
        ),
        migrations.RemoveField(
            model_name='incomesource',
            name='name',
        ),
    ]
