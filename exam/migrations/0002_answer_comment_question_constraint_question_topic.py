# Generated by Django 4.0.3 on 2022-04-11 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='comment',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='question',
            name='constraint',
            field=models.CharField(choices=[('NONE', 'None'), ('FOR', 'For Loop'), ('WHILE', 'While Loop'), ('IF', 'if')], default='NONE', max_length=10),
        ),
        migrations.AddField(
            model_name='question',
            name='topic',
            field=models.CharField(choices=[('MATH', 'Math'), ('ARRAYS', 'Arrays'), ('FORLOOP', 'For Loop'), ('WHILELOOP', 'While Loop'), ('RECURSION', 'Recursion'), ('IF', 'if')], default='MATH', max_length=10),
        ),
    ]
