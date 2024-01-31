# Generated by Django 4.2.9 on 2024-01-31 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_number', models.IntegerField(blank=True, null=True, verbose_name='Avto soni')),
                ('building_area', models.CharField(blank=True, max_length=100, null=True, verbose_name='Bino maydoni')),
                ('land_area', models.CharField(blank=True, max_length=100, null=True, verbose_name='Er maydoni')),
                ('address', models.CharField(blank=True, max_length=100, null=True, verbose_name='Manzili')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nomi')),
                ('number_of_employees', models.IntegerField(blank=True, null=True, verbose_name='Xodimlar soni')),
                ('completed_by_employee', models.CharField(blank=True, max_length=100, null=True, verbose_name='Toldirgan xodim')),
                ('filled_date', models.CharField(blank=True, max_length=100, null=True, verbose_name='Toldirilgan sana')),
            ],
            options={
                'verbose_name': 'Филиал',
                'verbose_name_plural': 'Филиалы',
            },
        ),
        migrations.CreateModel(
            name='TransportSketch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schetchik', models.IntegerField(blank=True, null=True, verbose_name='Schetchik')),
                ('soz', models.IntegerField(blank=True, null=True, verbose_name='soz')),
                ('nosoz', models.IntegerField(blank=True, null=True, verbose_name='nosoz')),
                ('xisobdan_chiqarish', models.IntegerField(blank=True, null=True, verbose_name='xisobdanChiqarish')),
                ('gps_ornatilgan', models.IntegerField(blank=True, null=True, verbose_name='gpsOrnatilgan')),
                ('dut_ornatilgan', models.IntegerField(blank=True, null=True, verbose_name='dutOrnatilgan')),
            ],
            options={
                'verbose_name': 'TransportSchetchik',
                'verbose_name_plural': 'TransportSchetchik',
            },
        ),
    ]