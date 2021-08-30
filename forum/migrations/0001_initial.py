# Generated by Django 3.2.6 on 2021-08-29 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('created', models.TimeField(auto_now_add=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created', models.TimeField(auto_now_add=True)),
                ('thread', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.thread')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.profile')),
            ],
        ),
    ]