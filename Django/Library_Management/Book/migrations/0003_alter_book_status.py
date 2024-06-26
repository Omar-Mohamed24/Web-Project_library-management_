# Generated by Django 5.0.6 on 2024-06-14 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0002_alter_book_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.CharField(choices=[('Available', 'Available'), ('Unavailable', 'Unavailable')], default='Available', max_length=30),
        ),
    ]