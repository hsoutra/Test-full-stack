# Generated by Django 4.2.3 on 2023-07-25 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acteur', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='actor',
            unique_together={('first_name', 'last_name')},
        ),
    ]
