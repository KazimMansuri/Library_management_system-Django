# Generated by Django 3.2.2 on 2021-05-10 07:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BOOK',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Book_name', models.CharField(max_length=100)),
                ('Book_description', models.TextField(max_length=250)),
                ('Category', models.CharField(choices=[('1', 'Ebook'), ('2', 'Hardcopy')], default=1, max_length=2)),
                ('Publish_Date', models.DateTimeField(default=django.utils.timezone.now)),
                ('Book_type', models.CharField(choices=[('1', 'sports'), ('2', 'educational'), ('3', 'motivational')], default=1, max_length=3)),
                ('Price', models.IntegerField()),
                ('Cover_page_img', models.ImageField(upload_to='cover_page/')),
            ],
        ),
    ]
