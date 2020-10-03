# Generated by Django 3.1.2 on 2020-10-03 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('learningMaterial', '0005_auto_20201003_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blurb',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blurb', to='learningMaterial.subject'),
        ),
        migrations.AlterField(
            model_name='lecturenote',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learningMaterial.subject'),
        ),
        migrations.AlterField(
            model_name='youtubevideo',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learningMaterial.subject'),
        ),
    ]