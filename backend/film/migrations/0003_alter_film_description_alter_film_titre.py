# Generated by Django 4.2.3 on 2023-07-25 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0002_film_description_film_titre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='film',
            name='titre',
            field=models.CharField(max_length=256),
        ),
    ]