# Generated by Django 3.1.2 on 2020-10-03 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learningMaterial', '0006_auto_20201003_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecturenote',
            name='favorites',
            field=models.IntegerField(default=0),
        ),
    ]
