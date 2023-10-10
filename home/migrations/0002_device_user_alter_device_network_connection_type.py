# Generated by Django 4.1.7 on 2023-06-15 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='devices', to='home.user'),
        ),
        migrations.AlterField(
            model_name='device',
            name='network_connection_type',
            field=models.CharField(choices=[('LAN', 'LAN'), ('Wifi', 'Wifi')], max_length=100),
        ),
    ]