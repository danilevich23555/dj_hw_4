# Generated by Django 3.1.2 on 2022-04-05 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0013_auto_20220405_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='scopes',
            field=models.ManyToManyField(related_name='scopes', through='articles.Relationship', to='articles.Scorpe'),
        ),
        migrations.AlterField(
            model_name='relationship',
            name='id_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tag', to='articles.scorpe'),
        ),
        migrations.AlterField(
            model_name='relationship',
            name='id_title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tag', to='articles.article'),
        ),
    ]