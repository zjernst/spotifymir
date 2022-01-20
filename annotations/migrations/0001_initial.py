# Generated by Django 4.0.1 on 2022-01-16 08:31

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spotify_id', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Annotation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mirex_mood', models.IntegerField(default=0)),
                ('valence', models.DecimalField(decimal_places=2, default=0, max_digits=3, validators=[django.core.validators.MaxValueValidator(1), django.core.validators.MinValueValidator(-1)])),
                ('energy', models.DecimalField(decimal_places=2, default=0, max_digits=3, validators=[django.core.validators.MaxValueValidator(1), django.core.validators.MinValueValidator(-1)])),
                ('amazement', models.BooleanField(default=False)),
                ('solemnity', models.BooleanField(default=False)),
                ('tenderness', models.BooleanField(default=False)),
                ('nostalgia', models.BooleanField(default=False)),
                ('calmness', models.BooleanField(default=False)),
                ('power', models.BooleanField(default=False)),
                ('joyful_activation', models.BooleanField(default=False)),
                ('tension', models.BooleanField(default=False)),
                ('sadness', models.BooleanField(default=False)),
                ('track', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='annotations.track')),
            ],
        ),
    ]
