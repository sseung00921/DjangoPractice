# Generated by Django 3.1.1 on 2020-10-05 07:29

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inflearn_lecture', '0003_auto_20201005_0630'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mytext',
            name='aa',
        ),
        migrations.AddField(
            model_name='mytext',
            name='board_text',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]