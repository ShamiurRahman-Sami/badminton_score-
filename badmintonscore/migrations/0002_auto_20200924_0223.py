# Generated by Django 3.1 on 2020-09-24 02:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('badmintonscore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_category', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='match',
            name='player_name',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='playernameB', to='badmintonscore.playername'),
        ),
        migrations.AlterField(
            model_name='match',
            name='match_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='badmintonscore.category'),
        ),
    ]