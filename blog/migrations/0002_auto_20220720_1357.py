# Generated by Django 3.0.14 on 2022-07-20 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_model',
            name='description',
            field=models.TextField(),
        ),
    ]