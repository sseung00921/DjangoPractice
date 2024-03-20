# Generated by Django 3.1.1 on 2020-10-06 02:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inflearn_lecture', '0007_auto_20201005_0930'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('writer', models.CharField(max_length=200, null=True)),
                ('rate', models.CharField(max_length=200, null=True)),
                ('comment', models.CharField(max_length=200, null=True)),
                ('lecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inflearn_lecture.mytext')),
            ],
        ),
    ]