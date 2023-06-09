# Generated by Django 4.2.1 on 2023-05-19 00:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('year', models.PositiveSmallIntegerField()),
                ('average_grade', models.DecimalField(decimal_places=2, max_digits=3)),
                ('average_confidence', models.DecimalField(decimal_places=2, max_digits=3)),
            ],
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('industry', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
                ('average_grade', models.DecimalField(decimal_places=2, max_digits=3)),
                ('average_confidence', models.DecimalField(decimal_places=2, max_digits=3)),
                ('frequency', models.IntegerField()),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reportinterview.book')),
            ],
        ),
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('grade', models.DecimalField(decimal_places=2, max_digits=3)),
                ('duration', models.IntegerField()),
                ('case_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reportinterview.case')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('case_count', models.IntegerField()),
                ('interviewee_time', models.IntegerField()),
                ('interviewer_time', models.IntegerField()),
                ('average_grade', models.DecimalField(decimal_places=2, max_digits=3)),
                ('average_confidence', models.DecimalField(decimal_places=2, max_digits=3)),
                ('is_admin', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Interviewer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Interviewer_notes', models.CharField(max_length=1000)),
                ('interview_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reportinterview.interview')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reportinterview.user')),
            ],
        ),
        migrations.CreateModel(
            name='Interviewee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('difficulty', models.IntegerField()),
                ('confidence', models.IntegerField()),
                ('interviewee_notes', models.CharField(max_length=1000)),
                ('interview_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reportinterview.interview')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reportinterview.user')),
            ],
        ),
        migrations.CreateModel(
            name='Case_Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('has_skill', models.BooleanField()),
                ('case_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reportinterview.case')),
                ('skill_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reportinterview.skill')),
            ],
        ),
    ]
