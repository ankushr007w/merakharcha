# Generated by Django 4.1.7 on 2024-10-13 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0002_expense_amount_alter_expense_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
