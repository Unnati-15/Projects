# Generated by Django 4.1.1 on 2023-01-22 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dog', '0009_alter_dogproduct_options'),
        ('cart', '0007_remove_pay_order_pay_cardno_pay_cvv_pay_month_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pay',
            name='products',
            field=models.ForeignKey(default='cart.models', on_delete=django.db.models.deletion.CASCADE, to='dog.dogproduct'),
        ),
    ]