# Generated by Django 3.1.7 on 2021-03-23 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='topping2',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]