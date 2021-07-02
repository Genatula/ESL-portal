# Generated by Django 3.2.4 on 2021-07-02 11:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=500)),
                ('answers_for_question', models.ManyToManyField(blank='True', null='True', related_name='all_questions', to='esl_app.Answer')),
                ('correct_answers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='correct_answer', to='esl_app.answer')),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_name', models.CharField(max_length=50)),
                ('test_description', models.CharField(max_length=1000)),
                ('test_short_description', models.CharField(max_length=200)),
                ('level', models.CharField(choices=[('A1', 'Elementary'), ('A2', 'Pre-Intermediate'), ('B1', 'Intermediate'), ('B2', 'Upper-Intermediate'), ('C1', 'Advanced'), ('C2', 'Proficiency')], max_length=2)),
                ('aspect', models.CharField(choices=[('LX', 'Lexis'), ('GR', 'Grammar')], max_length=2)),
                ('time_limit', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TestQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Single', 'Single choice question'), ('Insert', 'Question with insertion')], max_length=6)),
                ('questions_for_test', models.ManyToManyField(to='esl_app.Question')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='esl_app.test')),
            ],
        ),
        migrations.CreateModel(
            name='UserAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.CharField(max_length=30)),
                ('is_correct', models.BooleanField()),
                ('test_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='esl_app.testquestion')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Completion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_completed', models.BooleanField()),
                ('taken_time', models.PositiveIntegerField()),
                ('num_of_correct', models.PositiveSmallIntegerField()),
                ('is_started', models.BooleanField()),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='esl_app.test')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='question_for_answer',
            field=models.ManyToManyField(blank='True', null='True', to='esl_app.Question'),
        ),
    ]
