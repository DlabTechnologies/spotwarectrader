# Generated by Django 3.0.5 on 2020-10-18 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0027_auto_20201018_1635'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='gold',
            new_name='advanced',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='platinum',
            new_name='beginner',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='silver',
            new_name='expert',
        ),
        migrations.AddField(
            model_name='user',
            name='intermediate',
            field=models.BooleanField(default=False),
        ),
    ]
