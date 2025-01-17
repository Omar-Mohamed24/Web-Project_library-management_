# Generated by Django 5.0.6 on 2024-06-13 19:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Borrowing',
            fields=[
                ('borrow_id', models.AutoField(primary_key=True, serialize=False)),
                ('borrow_date', models.DateField()),
                ('return_date', models.DateField()),
                ('borrowed_book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='borrowings', to='Book.book')),
            ],
        ),
    ]
