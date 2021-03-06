# Generated by Django 2.0.5 on 2018-05-25 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pods', '0006_auto_20180525_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='podcast',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Author', to='pods.Author'),
        ),
        migrations.AlterField(
            model_name='podcastepisode',
            name='podcast',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Podcast', to='pods.Podcast'),
        ),
    ]
