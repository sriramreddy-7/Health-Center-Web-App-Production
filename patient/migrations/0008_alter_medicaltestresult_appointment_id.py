# Generated by Django 4.2.2 on 2023-07-16 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0007_medicaltestresult'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicaltestresult',
            name='appointment_id',
            field=models.CharField(max_length=20, primary_key=True, serialize=False, unique=True),
        ),
    ]