# Generated by Django 3.2.6 on 2021-08-08 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SomeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('some_field_str', models.CharField(max_length=255)),
                ('some_field_int', models.PositiveIntegerField()),
                ('some_field_boolean', models.BooleanField(default=False)),
            ],
        ),
    ]
