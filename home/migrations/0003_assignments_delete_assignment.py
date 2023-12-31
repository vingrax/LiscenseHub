# Generated by Django 4.1.7 on 2023-06-30 04:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_device_user_alter_device_network_connection_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assgned_device', to='home.device')),
                ('license', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assgnd_license', to='home.license')),
            ],
            options={
                'db_table': 'assignments',
            },
        ),
        migrations.DeleteModel(
            name='Assignment',
        ),
    ]
