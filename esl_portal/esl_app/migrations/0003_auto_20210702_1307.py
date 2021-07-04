# Generated by Django 2.2.20 on 2021-07-02 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('esl_app', '0002_auto_20210702_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='related_question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='esl_app.Question'),
        ),
        migrations.AlterField(
            model_name='question',
            name='correct_answer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='esl_app.Answer'),
        ),
    ]