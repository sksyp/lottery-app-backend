# Generated by Django 3.1.5 on 2021-01-15 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20210115_1932'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_winnings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_won', models.FloatField(null=True)),
                ('lobby_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='login.lobby_details')),
            ],
        ),
    ]
