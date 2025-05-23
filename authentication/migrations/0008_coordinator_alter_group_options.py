# Generated by Django 4.2.16 on 2024-11-03 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_group_ppt_group_report_group_working_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coordinator',
            fields=[
                ('cname', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=30, primary_key=True, serialize=False)),
                ('dept', models.CharField(max_length=60)),
                ('registered_academic_year', models.CharField(max_length=30)),
                ('registered_semester', models.IntegerField()),
                ('contact_num', models.FloatField()),
            ],
            options={
                'verbose_name_plural': 'Coordinators',
                'ordering': ['cname'],
            },
        ),
        migrations.AlterModelOptions(
            name='group',
            options={'ordering': ['sname'], 'verbose_name_plural': 'Groups'},
        ),
    ]
