# Generated by Django 3.0.4 on 2020-09-15 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='feedback_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('role', models.CharField(choices=[('Intern', 'Intern'), ('Mentor', 'Mentor')], max_length=200)),
                ('feedback', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'FEEDBACK',
            },
        ),
        migrations.CreateModel(
            name='transaction_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_email', models.EmailField(max_length=320)),
                ('to_email', models.EmailField(max_length=320)),
                ('date', models.DateField(max_length=20)),
                ('credit', models.BigIntegerField()),
                ('current_time', models.TimeField()),
            ],
            options={
                'verbose_name_plural': 'TRANSACTIONS HISTORY',
            },
        ),
        migrations.CreateModel(
            name='user_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.BigIntegerField()),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=320)),
                ('credit', models.BigIntegerField()),
            ],
            options={
                'verbose_name_plural': 'USERS',
            },
        ),
    ]
