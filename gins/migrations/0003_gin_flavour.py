# Generated by Django 3.2.7 on 2021-09-09 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gins', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='gin',
            name='flavour',
            field=models.CharField(default='Classic', max_length=10),
            preserve_default=False,
        ),
    ]