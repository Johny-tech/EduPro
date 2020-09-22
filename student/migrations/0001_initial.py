# Generated by Django 3.1 on 2020-09-21 07:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoneHomework',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('done', models.BooleanField(default=False)),
                ('checked', models.BooleanField(default=False)),
                ('checkedDate', models.DateField(null=True)),
                ('note', models.CharField(blank=True, max_length=255)),
                ('mark', models.IntegerField(default=0)),
                ('homework', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='done_homework', to='teacher.homework')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.student')),
            ],
        ),
        migrations.CreateModel(
            name='ImagesHomework',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('photo', models.ImageField(upload_to='homework/')),
                ('done_homework', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.donehomework')),
            ],
        ),
        migrations.CreateModel(
            name='EnrolledTesting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.IntegerField(default=0)),
                ('started', models.DateTimeField()),
                ('istaken', models.BooleanField(default=False)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.student')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test', to='accounts.test')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.IntegerField()),
                ('enrolledTesting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.enrolledtesting')),
            ],
        ),
    ]
