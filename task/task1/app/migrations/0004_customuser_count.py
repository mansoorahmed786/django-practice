# Generated by Django 4.2.5 on 2023-09-21 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_book_remove_customuser_ip_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='count',
            field=models.IntegerField(default=0, editable=False),
        ),
    ]
