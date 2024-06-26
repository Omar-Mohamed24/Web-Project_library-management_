# Generated by Django 5.0.6 on 2024-06-13 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('book_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('publisher', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=100)),
                ('isbn', models.CharField(max_length=25)),
                ('pages', models.IntegerField(blank=True, null=True)),
                ('rating', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
                ('edition', models.CharField(blank=True, max_length=50, null=True)),
                ('about', models.TextField(blank=True, null=True)),
                ('summary', models.TextField(blank=True, null=True)),
                ('cover', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(max_length=30)),
            ],
        ),
    ]
