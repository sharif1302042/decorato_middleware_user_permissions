# Generated by Django 2.2 on 2019-04-16 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BANK', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tranferbalance',
            name='credit_account',
        ),
        migrations.RemoveField(
            model_name='tranferbalance',
            name='debit_account',
        ),
        migrations.DeleteModel(
            name='Topup',
        ),
        migrations.DeleteModel(
            name='TranferBalance',
        ),
    ]