# Generated by Django 4.0.2 on 2022-07-02 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='marks',
            field=models.IntegerField(blank=True, default=None),
        ),
    ]