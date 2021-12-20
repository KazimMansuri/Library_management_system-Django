# Generated by Django 3.2.2 on 2021-05-10 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0002_auto_20210510_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='Book_type',
            field=models.CharField(choices=[('1', 'sports'), ('2', 'educational'), ('3', 'motivational')], default=1, max_length=3),
        ),
        migrations.AlterField(
            model_name='book',
            name='Category',
            field=models.CharField(choices=[('1', 'Ebook'), ('2', 'Hardcopy')], default=1, max_length=2),
        ),
    ]
