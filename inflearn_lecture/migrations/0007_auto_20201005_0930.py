# Generated by Django 3.1.1 on 2020-10-05 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inflearn_lecture', '0006_mytext_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mytext',
            name='img_url',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
