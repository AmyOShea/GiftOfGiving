# Generated by Django 3.2 on 2021-12-13 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_alter_profile_organisation_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='organisation_name',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]