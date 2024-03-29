# Generated by Django 4.2.9 on 2024-01-31 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_qoshimchamalumotlar_spidometrkorsatgichi_texnikkorik_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test_Filiallar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avto_soni', models.CharField(blank=True, max_length=100, null=True, verbose_name='avto_soni')),
                ('bino_maydoni', models.CharField(blank=True, max_length=100, null=True, verbose_name='bino_maydoni')),
                ('er_maydoni', models.CharField(blank=True, max_length=100, null=True, verbose_name='er_maydoni')),
                ('manzili', models.CharField(blank=True, max_length=100, null=True, verbose_name='manzili')),
                ('nomi', models.CharField(blank=True, max_length=100, null=True, verbose_name='nomi')),
                ('toldirganXodim', models.CharField(blank=True, max_length=100, null=True, verbose_name='toldirganXodim')),
                ('toldirilganSana', models.CharField(blank=True, max_length=100, null=True, verbose_name='toldirilganSana')),
                ('xodimlar_soni', models.CharField(blank=True, max_length=100, null=True, verbose_name='xodimlar_soni')),
                ('xaydovchilar_soni', models.CharField(blank=True, max_length=100, null=True, verbose_name='xaydovchilar_soni')),
                ('yuqoriTashkilot', models.CharField(blank=True, max_length=100, null=True, verbose_name='yuqoriTashkilot')),
            ],
            options={
                'verbose_name': 'Test_Filiallar',
                'verbose_name_plural': 'Test_Filiallar',
            },
        ),
        migrations.CreateModel(
            name='Test_Transport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tashkilot', models.CharField(blank=True, max_length=200, null=True, verbose_name='tashkilot')),
                ('turi', models.CharField(blank=True, max_length=200, null=True, verbose_name='turi')),
                ('rusumi', models.CharField(blank=True, max_length=200, null=True, verbose_name='rusumi')),
                ('gosNomeri', models.CharField(blank=True, max_length=200, null=True, verbose_name='gosNomeri')),
                ('xaydovchi', models.CharField(blank=True, max_length=200, null=True, verbose_name='xaydovchi')),
                ('texPasportSeria', models.CharField(blank=True, max_length=200, null=True, verbose_name='texPasportSeria')),
                ('texPasportBerilganSana', models.CharField(blank=True, max_length=200, null=True, verbose_name='texPasportBerilganSana')),
                ('sugurtaRaqami', models.CharField(blank=True, max_length=200, null=True, verbose_name='sugurtaRaqami')),
                ('sugurtaAmalMuddati', models.CharField(blank=True, max_length=200, null=True, verbose_name='sugurtaAmalMuddati')),
                ('ishlabChiqYili', models.CharField(blank=True, max_length=200, null=True, verbose_name='ishlabChiqYili')),
                ('yukKotarishXajmi', models.CharField(blank=True, max_length=200, null=True, verbose_name='yukKotarishXajmi')),
                ('biriktirilganUMG', models.CharField(blank=True, max_length=200, null=True, verbose_name='biriktirilganUMG')),
                ('gpsOrnatilganBool', models.CharField(blank=True, max_length=200, null=True, verbose_name='gpsOrnatilganBool')),
                ('dutOrnatilgan', models.CharField(blank=True, max_length=200, null=True, verbose_name='dutOrnatilgan')),
                ('avtoXolati', models.CharField(blank=True, max_length=200, null=True, verbose_name='avtoXolati')),
                ('avtoXisobdanChiqarish', models.CharField(blank=True, max_length=200, null=True, verbose_name='avtoXisobdanChiqarish')),
                ('yoqilgi', models.CharField(blank=True, max_length=200, null=True, verbose_name='yoqilgi')),
                ('toldirganXodim', models.CharField(blank=True, max_length=200, null=True, verbose_name='toldirganXodim')),
                ('toldirilganSana', models.CharField(blank=True, max_length=200, null=True, verbose_name='toldirilganSana')),
            ],
            options={
                'verbose_name': 'Test_Transport_Model',
                'verbose_name_plural': 'Test_Transport_Model',
            },
        ),
        migrations.CreateModel(
            name='Test_Xaydovchilar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tashkilot', models.CharField(blank=True, max_length=100, null=True, verbose_name='tashkilot')),
                ('familiasi', models.CharField(blank=True, max_length=100, null=True, verbose_name='familiasi')),
                ('ismi', models.CharField(blank=True, max_length=100, null=True, verbose_name='ismi')),
                ('otasini_ismi', models.CharField(blank=True, max_length=100, null=True, verbose_name='otasini_ismi')),
                ('pasp_raqami', models.CharField(blank=True, max_length=100, null=True, verbose_name='pasp_raqami')),
                ('pasp_berilgan', models.CharField(blank=True, max_length=100, null=True, verbose_name='pasp_berilgan')),
                ('pasp_amal', models.CharField(blank=True, max_length=100, null=True, verbose_name='pasp_amal')),
                ('prava_raqami', models.CharField(blank=True, max_length=100, null=True, verbose_name='prava_raqami')),
                ('prava_berilgan', models.CharField(blank=True, max_length=100, null=True, verbose_name='prava_berilgan')),
                ('prava_amal', models.CharField(blank=True, max_length=100, null=True, verbose_name='prava_amal')),
                ('toldirganXodim', models.CharField(blank=True, max_length=100, null=True, verbose_name='toldirganXodim')),
                ('toldirilganSana', models.CharField(blank=True, max_length=100, null=True, verbose_name='toldirilganSana')),
            ],
            options={
                'verbose_name': 'Test_Xaydovchilar',
                'verbose_name_plural': 'Test_Xaydovchilar',
            },
        ),
        migrations.CreateModel(
            name='Test_Xodimlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tashkilot', models.CharField(blank=True, max_length=100, null=True, verbose_name='tashkilot')),
                ('familia', models.CharField(blank=True, max_length=100, null=True, verbose_name='familia')),
                ('ismi', models.CharField(blank=True, max_length=100, null=True, verbose_name='ismi')),
                ('otasiniIsmi', models.CharField(blank=True, max_length=100, null=True, verbose_name='otasiniIsmi')),
                ('lavozimi', models.CharField(blank=True, max_length=100, null=True, verbose_name='lavozimi')),
                ('lavozimiKey', models.CharField(blank=True, max_length=100, null=True, verbose_name='lavozimiKey')),
                ('mutaxasisligi', models.CharField(blank=True, max_length=100, null=True, verbose_name='mutaxasisligi')),
                ('tel', models.CharField(blank=True, max_length=100, null=True, verbose_name='tel')),
                ('toldirganXodim', models.CharField(blank=True, max_length=100, null=True, verbose_name='toldirganXodim')),
                ('toldirilganSana', models.CharField(blank=True, max_length=100, null=True, verbose_name='toldirilganSana')),
            ],
            options={
                'verbose_name': 'Test_Xodimlar',
                'verbose_name_plural': 'Test_Xodimlar',
            },
        ),
    ]
