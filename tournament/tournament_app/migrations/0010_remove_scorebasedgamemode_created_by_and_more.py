# Generated by Django 5.0.6 on 2024-06-24 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament_app', '0009_bracket'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scorebasedgamemode',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='timebasedgamemode',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='tournament',
            name='game_mode_id',
        ),
        migrations.RemoveField(
            model_name='tournament',
            name='game_mode_type',
        ),
        migrations.AddField(
            model_name='tournament',
            name='game_mode',
            field=models.CharField(choices=[('TimeAttack', 'Time Attack'), ('HighestScore', 'Highest Score')], default='TimeAttack', max_length=20),
        ),
        migrations.AddField(
            model_name='tournament',
            name='rounds',
            field=models.IntegerField(choices=[(1, '1 Round'), (2, '2 Rounds'), (3, '3 Rounds')], default=1, help_text='Number of rounds'),
        ),
        migrations.DeleteModel(
            name='HybridGameMode',
        ),
        migrations.DeleteModel(
            name='ScoreBasedGameMode',
        ),
        migrations.DeleteModel(
            name='TimeBasedGameMode',
        ),
    ]