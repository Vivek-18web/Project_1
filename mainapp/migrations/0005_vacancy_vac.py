# Generated by Django 5.1.4 on 2024-12-25 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_rename_skiil_berojgar_skill_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='vac',
            field=models.CharField(default=1, max_length=10),
        ),
    ]
