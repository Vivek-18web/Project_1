# Generated by Django 4.2.17 on 2025-01-10 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0021_alter_application_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='photo',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
