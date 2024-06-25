# Generated by Django 5.0.6 on 2024-06-25 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament_app', '0018_rename_coach_team_guardian_contact_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='guardian_name',
            new_name='coach',
        ),
        migrations.RemoveField(
            model_name='team',
            name='guardian_contact',
        ),
        migrations.AddField(
            model_name='team',
            name='time_total_score',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='total_score',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tournament',
            name='description',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='time_score_one',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='time_score_three',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='time_score_two',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='game_mode',
            field=models.CharField(choices=[('TimeAttack', 'Time Attack: Complete the objective in the shortest time possible.'), ('HighestScore', 'Highest Score: Achieve the highest score to win.')], default='TimeAttack', max_length=20),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='rounds',
            field=models.IntegerField(choices=[(1, '1 Round'), (2, '2 Rounds'), (3, '3 Rounds')], default=1, help_text='Number of rounds'),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='rules',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
