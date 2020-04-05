# Generated by Django 3.0.4 on 2020-03-31 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('age', models.IntegerField(default=0)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=6)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zeCompany.Company')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zeCompany.Department')),
            ],
        ),
    ]