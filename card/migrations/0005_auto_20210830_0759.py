# Generated by Django 3.2.6 on 2021-08-30 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0004_auto_20210830_0645'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='response',
            name='owner',
        ),
        migrations.AddField(
            model_name='response',
            name='post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='card.post'),
            preserve_default=False,
        ),
    ]