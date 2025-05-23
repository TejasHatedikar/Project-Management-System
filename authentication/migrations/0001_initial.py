# Generated by Django 4.2.16 on 2024-10-11 07:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('fname', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=30, primary_key=True, serialize=False)),
                ('dept', models.CharField(max_length=60)),
                ('registered_academic_year', models.CharField(max_length=30)),
                ('registered_semester', models.IntegerField()),
                ('contact_num', models.FloatField()),
            ],
            options={
                'verbose_name_plural': 'Faculties',
                'ordering': ['fname'],
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('sname', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('dept', models.CharField(max_length=60)),
                ('academic_year', models.CharField(max_length=10)),
                ('registered_semester', models.IntegerField()),
                ('div', models.CharField(max_length=10)),
                ('prn', models.BigIntegerField()),
                ('roll', models.BigIntegerField()),
                ('contact_num', models.FloatField()),
                ('group_id', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('memName1', models.CharField(max_length=30)),
                ('memPRN1', models.BigIntegerField()),
                ('memRoll1', models.BigIntegerField()),
                ('memName2', models.CharField(max_length=30)),
                ('memPRN2', models.BigIntegerField()),
                ('memRoll2', models.BigIntegerField()),
                ('memName3', models.CharField(max_length=30)),
                ('memPRN3', models.BigIntegerField()),
                ('memRoll3', models.BigIntegerField()),
            ],
            options={
                'ordering': ['sname'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Tags',
                'ordering': ['tag'],
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('project_id', models.AutoField(primary_key=True, serialize=False)),
                ('pname', models.CharField(max_length=100)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.student')),
                ('tags', models.ManyToManyField(to='authentication.tag')),
            ],
            options={
                'verbose_name_plural': 'Projects',
                'ordering': ['pname'],
            },
        ),
    ]
