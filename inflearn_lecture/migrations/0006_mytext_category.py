# Generated by Django 3.1.1 on 2020-10-05 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inflearn_lecture', '0005_auto_20201005_0731'),
    ]

    operations = [
        migrations.AddField(
            model_name='mytext',
            name='category',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
