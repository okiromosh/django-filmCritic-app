# Generated by Django 4.2.6 on 2023-10-19 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_myuser_bio_alter_myuser_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.type'),
        ),
    ]
