# Generated by Django 5.1.2 on 2024-11-12 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0006_alter_activity_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='activity_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
