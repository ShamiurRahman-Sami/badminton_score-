# Generated by Django 2.2.8 on 2020-11-10 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('badmintonscore', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teamnames',
            old_name='ranking',
            new_name='point',
        ),
        migrations.AddField(
            model_name='teamnames',
            name='Group',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B')], default='A', max_length=2),
            preserve_default=False,
        ),
    ]
