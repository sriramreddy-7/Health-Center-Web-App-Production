# Generated by Django 4.2.2 on 2023-07-06 15:20

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_alter_ft_patient_token'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('patient_token', models.CharField(max_length=10, unique=True)),
                ('appointment_id', models.CharField(max_length=15, primary_key=True, serialize=False, unique=True)),
                ('visit_date', models.DateField()),
                ('doctor_name', models.CharField(max_length=100)),
                ('patient_type', models.CharField(max_length=100)),
                ('doctor_fee', models.DecimalField(decimal_places=2, max_digits=10)),
                ('gst', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('today_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patientprimarydata')),
            ],
        ),
    ]
