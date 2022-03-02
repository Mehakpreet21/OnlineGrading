# Generated by Django 4.0.2 on 2022-03-02 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0003_question_difficulty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='difficulty',
            field=models.CharField(choices=[('EASY', 'EASY'), ('MEDIUM', 'MEDIUM'), ('HARD', 'HARD')], default='EASY', max_length=10),
        ),
    ]
