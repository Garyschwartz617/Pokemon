# Generated by Django 3.2.6 on 2021-08-31 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('card', '0009_alter_response_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='response',
            name='amount',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='response',
            name='card_buyer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='card.singular'),
        ),
        migrations.CreateModel(
            name='BalanceUpdate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=50)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='amount', to='accounts.profile')),
            ],
        ),
    ]
