from django.db import models


class Branch(models.Model):
    car_number = models.IntegerField(verbose_name='Avto soni', blank=True, null=True)
    building_area = models.CharField(verbose_name='Bino maydoni', max_length=100, blank=True, null=True)
    land_area = models.CharField(max_length=100, verbose_name='Er maydoni', null=True, blank=True)
    address = models.CharField(max_length=100, verbose_name='Manzili', null=True, blank=True)
    name = models.CharField(max_length=100, verbose_name='Nomi', null=True, blank=True)
    number_of_employees = models.IntegerField(verbose_name='Xodimlar soni', null=True, blank=True)
    completed_by_employee = models.CharField(verbose_name='Toldirgan xodim', max_length=100, null=True, blank=True)
    filled_date = models.CharField(verbose_name='Toldirilgan sana', max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Филиал'
        verbose_name_plural = 'Филиалы'


class TransportSketch(models.Model):
    schetchik = models.IntegerField(verbose_name='Schetchik', null=True, blank=True)
    soz = models.IntegerField(verbose_name='soz', null=True, blank=True)
    nosoz = models.IntegerField(verbose_name='nosoz', null=True, blank=True)
    xisobdan_chiqarish = models.IntegerField(verbose_name='xisobdanChiqarish', null=True, blank=True)
    gps_ornatilgan = models.IntegerField(verbose_name='gpsOrnatilgan', null=True, blank=True)
    dut_ornatilgan = models.IntegerField(verbose_name='dutOrnatilgan', null=True, blank=True)

    def __str__(self):
        return str(self.schetchik)

    class Meta:
        verbose_name = 'TransportSchetchik'
        verbose_name_plural = 'TransportSchetchik'


class TSModeli(models.Model):
    img = models.ImageField(verbose_name='img', null=True, blank=True, upload_to='images/')
    gosRaqami = models.CharField(verbose_name='gosRaqami', null=True, blank=True, max_length=100)
    rusumi = models.CharField(verbose_name='rusumi', null=True, blank=True, max_length=100)
    rangi = models.CharField(verbose_name='rangi', null=True, blank=True, max_length=100)
    egasi = models.CharField(verbose_name='egasi', null=True, blank=True, max_length=100)
    manzili = models.CharField(verbose_name='manzili', null=True, blank=True, max_length=100)
    berilganSanasi = models.CharField(verbose_name='berilganSanasi', null=True, blank=True, max_length=100)
    yhxBolimi = models.CharField(verbose_name='yhxBolimi', null=True, blank=True, max_length=100)
    inn = models.CharField(verbose_name='inn', null=True, blank=True, max_length=100)
    ishlabChiqarilganYili = models.CharField(verbose_name='ishlabChiqarilganYili', null=True, blank=True,
                                             max_length=100)
    turi = models.CharField(verbose_name='turi', null=True, blank=True, max_length=100)
    kuzovRaqami = models.CharField(verbose_name='kuzovRaqami', null=True, blank=True, max_length=100)
    shassiRaqami = models.CharField(verbose_name='shassiRaqami', null=True, blank=True, max_length=100)
    tolaVazni = models.CharField(verbose_name='tolaVazni', null=True, blank=True, max_length=100)
    yuksizVazni = models.CharField(verbose_name='yuksizVazni', null=True, blank=True, max_length=100)
    dvigatelRaqami = models.CharField(verbose_name='dvigatelRaqami', null=True, blank=True, max_length=100)
    dvigatelQuvvati = models.CharField(verbose_name='dvigatelQuvvati', null=True, blank=True, max_length=100)
    yonilgiTuri = models.CharField(verbose_name='yonilgiTuri', null=True, blank=True, max_length=100)
    otiradiganJoylari = models.CharField(verbose_name='otiradiganJoylari', null=True, blank=True, max_length=100)
    tikTuradiganJoylari = models.CharField(verbose_name='tikTuradiganJoylari', null=True, blank=True, max_length=100)
    alohidaBelgilari = models.CharField(verbose_name='alohidaBelgilari', null=True, blank=True, max_length=100)
    biriktirilganXodim = models.CharField(verbose_name='biriktirilganXodim', null=True, blank=True, max_length=100)
    biriktirilganUMG = models.CharField(verbose_name='biriktirilganUMG', null=True, blank=True, max_length=100)
    sugurtaNomeri = models.CharField(verbose_name='sugurtaNomeri', null=True, blank=True, max_length=100)
    sugurtaTugashKuni = models.CharField(verbose_name='sugurtaTugashKuni', null=True, blank=True, max_length=100)
    sugurtaKompaniyasi = models.CharField(verbose_name='sugurtaKompaniyasi', null=True, blank=True, max_length=100)
    gpsBool = models.BooleanField(verbose_name='gpsBool', null=True, blank=True, )
    dutBool = models.BooleanField(verbose_name='dutBool', null=True, blank=True, )
    xisobdanChiqarish = models.BooleanField(verbose_name='xisobdanChiqarish', null=True, blank=True, )
    yurKotarishKG = models.CharField(verbose_name='yurKotarishKG', null=True, blank=True, max_length=100)
    texnikXolati = models.CharField(verbose_name='texnikXolati', null=True, blank=True, max_length=100)

    class Meta:
        verbose_name = 'TSModeli'
        verbose_name_plural = 'TSModeli'


class QoshimchaMalumotlar(models.Model):
    ozgartirganXodim = models.CharField(verbose_name='ozgartirganXodim', max_length=100, null=True, blank=True)
    qowimchaMalumotlar = models.CharField(verbose_name='qowimchaMalumotlar', max_length=100, null=True, blank=True)
    sana = models.CharField(verbose_name='sana', max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = 'QoshimchaMalumotlar'
        verbose_name_plural = 'QoshimchaMalumotlar'


class SpidometrKorsatgichi(models.Model):
    spidometrKorsatgichi = models.CharField(verbose_name='spidometrKorsatgichi', max_length=100, null=True, blank=True)
    sana = models.CharField(verbose_name='sana', max_length=100, null=True, blank=True)
    ozgartirganXodim = models.CharField(verbose_name='ozgartirganXodim', max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = 'SpidometrKorsatgichi'
        verbose_name_plural = 'SpidometrKorsatgichi'


class TexnikKorik(models.Model):
    ozgartirganXodim = models.CharField(verbose_name='ozgartirganXodim', max_length=100, null=True, blank=True)
    sana = models.CharField(verbose_name='sana', max_length=100, null=True, blank=True)
    xarajatQiymati = models.CharField(verbose_name='xarajatQiymati', max_length=100, null=True, blank=True)
    oxirgiKorikdanOtganSana = models.CharField(verbose_name='oxirgiKorikdanOtganSana', max_length=100, null=True,
                                               blank=True)

    class Meta:
        verbose_name = 'TexnikKorik'
        verbose_name_plural = 'TexnikKorik'


class AlmashtirilganZapchastRoyxati(models.Model):
    texnik_korik = models.ForeignKey(TexnikKorik, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(verbose_name='almashtirilganZapchastRoyxati', max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = 'AlmashtirilganZapchastRoyxati'
        verbose_name_plural = 'AlmashtirilganZapchastRoyxati'


class YoqilgiOstatkasi(models.Model):
    qoldiq = models.CharField(verbose_name='qoldiq', max_length=100, null=True, blank=True)
    sana = models.CharField(verbose_name='sana', max_length=100, null=True, blank=True)
    ozgartirganXodim = models.CharField(verbose_name='ozgartirganXodim', max_length=100, null=True, blank=True)
    narxi = models.CharField(verbose_name='narxi', max_length=100, null=True, blank=True)
    yoqilgiTuri = models.CharField(verbose_name='yoqilgiTuri', max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = 'YoqilgiOstatkasi'
        verbose_name_plural = 'YoqilgiOstatkasi'


class Zapchast(models.Model):
    ozgartirganXodim = models.CharField(verbose_name='ozgartirganXodim', max_length=100, null=True, blank=True)
    sana = models.CharField(verbose_name='sana', max_length=100, null=True, blank=True)
    xarajatQiymati = models.CharField(verbose_name='xarajatQiymati', max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = 'Zapchast'
        verbose_name_plural = 'Zapchast'


class AlmashtirilganZapchastRoyxati2(models.Model):
    zapchast = models.ForeignKey(Zapchast, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(verbose_name='almashtirilganZapchastRoyxati', max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = 'AlmashtirilganZapchastRoyxati'
        verbose_name_plural = 'AlmashtirilganZapchastRoyxati'


class Test_Filiallar(models.Model):
    avto_soni = models.CharField(verbose_name='avto_soni', max_length=100, null=True, blank=True)
    bino_maydoni = models.CharField(verbose_name='bino_maydoni', max_length=100, null=True, blank=True)
    er_maydoni = models.CharField(verbose_name='er_maydoni', max_length=100, null=True, blank=True)
    manzili = models.CharField(verbose_name='manzili', max_length=100, null=True, blank=True)
    nomi = models.CharField(verbose_name='nomi', max_length=100, null=True, blank=True)
    toldirganXodim = models.CharField(verbose_name='toldirganXodim', max_length=100, null=True, blank=True)
    toldirilganSana = models.CharField(verbose_name='toldirilganSana', max_length=100, null=True, blank=True)
    xodimlar_soni = models.CharField(verbose_name='xodimlar_soni', max_length=100, null=True, blank=True)
    xaydovchilar_soni = models.CharField(verbose_name='xaydovchilar_soni', max_length=100, null=True, blank=True)
    yuqoriTashkilot = models.CharField(verbose_name='yuqoriTashkilot', max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = 'Test_Filiallar'
        verbose_name_plural = 'Test_Filiallar'


class Test_Xodimlar(models.Model):
    tashkilot = models.CharField(verbose_name='tashkilot', max_length=100, null=True, blank=True)
    familia = models.CharField(verbose_name='familia', max_length=100, null=True, blank=True)
    ismi = models.CharField(verbose_name='ismi', max_length=100, null=True, blank=True)
    otasiniIsmi = models.CharField(verbose_name='otasiniIsmi', max_length=100, null=True, blank=True)
    lavozimi = models.CharField(verbose_name='lavozimi', max_length=100, null=True, blank=True)
    lavozimiKey = models.CharField(verbose_name='lavozimiKey', max_length=100, null=True, blank=True)
    mutaxasisligi = models.CharField(verbose_name='mutaxasisligi', max_length=100, null=True, blank=True)
    tel = models.CharField(verbose_name='tel', max_length=100, null=True, blank=True)
    toldirganXodim = models.CharField(verbose_name='toldirganXodim', max_length=100, null=True, blank=True)
    toldirilganSana = models.CharField(verbose_name='toldirilganSana', max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = 'Test_Xodimlar'
        verbose_name_plural = 'Test_Xodimlar'


class Test_Xaydovchilar(models.Model):
    tashkilot = models.CharField(verbose_name='tashkilot', max_length=100, null=True, blank=True)
    familiasi = models.CharField(verbose_name='familiasi', max_length=100, null=True, blank=True)
    ismi = models.CharField(verbose_name='ismi', max_length=100, null=True, blank=True)
    otasini_ismi = models.CharField(verbose_name='otasini_ismi', max_length=100, null=True, blank=True)
    pasp_raqami = models.CharField(verbose_name='pasp_raqami', max_length=100, null=True, blank=True)
    pasp_berilgan = models.CharField(verbose_name='pasp_berilgan', max_length=100, null=True, blank=True)
    pasp_amal = models.CharField(verbose_name='pasp_amal', max_length=100, null=True, blank=True)
    prava_raqami = models.CharField(verbose_name='prava_raqami', max_length=100, null=True, blank=True)
    prava_berilgan = models.CharField(verbose_name='prava_berilgan', max_length=100, null=True, blank=True)
    prava_amal = models.CharField(verbose_name='prava_amal', max_length=100, null=True, blank=True)
    toldirganXodim = models.CharField(verbose_name='toldirganXodim', max_length=100, null=True, blank=True)
    toldirilganSana = models.CharField(verbose_name='toldirilganSana', max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = 'Test_Xaydovchilar'
        verbose_name_plural = 'Test_Xaydovchilar'


class Test_Transport(models.Model):
    tashkilot = models.CharField(max_length=200, verbose_name='tashkilot', null=True, blank=True)
    turi = models.CharField(max_length=200, verbose_name='turi', null=True, blank=True)
    rusumi = models.CharField(max_length=200, verbose_name='rusumi', null=True, blank=True)
    gosNomeri = models.CharField(max_length=200, verbose_name='gosNomeri', null=True, blank=True)
    xaydovchi = models.CharField(max_length=200, verbose_name='xaydovchi', null=True, blank=True)
    texPasportSeria = models.CharField(max_length=200, verbose_name='texPasportSeria', null=True, blank=True)
    texPasportBerilganSana = models.CharField(max_length=200, verbose_name='texPasportBerilganSana', null=True,
                                              blank=True)
    sugurtaRaqami = models.CharField(max_length=200, verbose_name='sugurtaRaqami', null=True, blank=True)
    sugurtaAmalMuddati = models.CharField(max_length=200, verbose_name='sugurtaAmalMuddati', null=True, blank=True)
    ishlabChiqYili = models.CharField(max_length=200, verbose_name='ishlabChiqYili', null=True, blank=True)
    yukKotarishXajmi = models.CharField(max_length=200, verbose_name='yukKotarishXajmi', null=True, blank=True)
    biriktirilganUMG = models.CharField(max_length=200, verbose_name='biriktirilganUMG', null=True, blank=True)
    gpsOrnatilganBool = models.CharField(max_length=200, verbose_name='gpsOrnatilganBool', null=True, blank=True)
    dutOrnatilgan = models.CharField(max_length=200, verbose_name='dutOrnatilgan', null=True, blank=True)
    avtoXolati = models.CharField(max_length=200, verbose_name='avtoXolati', null=True, blank=True)
    avtoXisobdanChiqarish = models.CharField(max_length=200, verbose_name='avtoXisobdanChiqarish', null=True,
                                             blank=True)
    yoqilgi = models.CharField(max_length=200, verbose_name='yoqilgi', null=True, blank=True)
    toldirganXodim = models.CharField(max_length=200, verbose_name='toldirganXodim', null=True, blank=True)
    toldirilganSana = models.CharField(max_length=200, verbose_name='toldirilganSana', null=True, blank=True)

    class Meta:
        verbose_name = 'Test_Transport_Model'
        verbose_name_plural = 'Test_Transport_Model'


class PutevoyList(models.Model):
    putevoyniTuzganXodim = models.CharField(verbose_name='putevoyniTuzganXodim', max_length=200, null=True, blank=True)
    tashkilot = models.CharField(verbose_name='tashkilot', max_length=200, null=True, blank=True)
    mexanikFIO = models.CharField(verbose_name='mexanikFIO', max_length=200, null=True, blank=True)
    mexanikTasdiqladi = models.BooleanField(verbose_name='mexanikTasdiqladi', null=True, blank=True)
    mexanikTasdiqlaganVaqti = models.CharField(verbose_name='mexanikTasdiqladi', max_length=200, null=True, blank=True)
    vrachFIO = models.CharField(verbose_name='vrachFIO', null=True, blank=True, max_length=200)
    vrachTasdiqladi = models.BooleanField(verbose_name='vrachTasdiqladi', null=True, blank=True, )
    vrachTasdiqlaganVaqti = models.CharField(verbose_name='vrachTasdiqlaganVaqti', null=True, blank=True,
                                             max_length=200)
    vrachQaytgandaFIO = models.CharField(verbose_name='vrachQaytgandaFIO', blank=True, null=True, max_length=200)
    vrachQaytgandaTasdiqladi = models.BooleanField(verbose_name='vrachQaytgandaTasdiqladi', blank=True, null=True)
    vrachQaytgandaTasdiqlaganVaqti = models.CharField(verbose_name='vrachQaytgandaTasdiqlaganVaqti', blank=True,
                                                      null=True, max_length=200)
    injinerFIO = models.CharField(verbose_name='injinerFIO', null=True, blank=True, max_length=200)
    injinerTasdiqladi = models.BooleanField(verbose_name='injinerTasdiqladi', null=True, blank=True)
    injinerTasdiqlaganVaqti = models.CharField(verbose_name='injinerTasdiqlaganVaqti', null=True, blank=True,
                                               max_length=200)
    nachalnikFIO = models.CharField(verbose_name='nachalnikFIO', null=True, blank=True, max_length=200)
    nachalnikTasdiqladi = models.BooleanField(verbose_name='nachalnikTasdiqladi', null=True, blank=True)
    nachalnikTasdiqlaganVaqti = models.CharField(verbose_name='nachalnikTasdiqlaganVaqti', null=True, blank=True,
                                                 max_length=200)
    dispecherFIO = models.CharField(verbose_name='dispecherFIO', null=True, blank=True, max_length=200)
    dispecherTasdiqladi = models.BooleanField(verbose_name='dispecherTasdiqladi', null=True, blank=True, )
    dispecherTasdiqlaganVaqti = models.CharField(verbose_name='dispecherTasdiqlaganVaqti', null=True, blank=True,
                                                 max_length=200)
    xaydovchiFIO = models.CharField(verbose_name='xaydovchiFIO', null=True, blank=True, max_length=200)
    xaydovchi2 = models.CharField(verbose_name='xaydovchi2', null=True, blank=True, max_length=200)
    xaydovchi3 = models.CharField(verbose_name='xaydovchi3', null=True, blank=True, max_length=200)
    xaydochiTasdiqladi = models.BooleanField(verbose_name='xaydochiTasdiqladi', null=True, blank=True)
    xaydochiTasdiqlaganVaqti = models.CharField(verbose_name='xaydochiTasdiqlaganVaqti', null=True, blank=True,
                                                max_length=200)
    xaydovchiPravaRaqami = models.CharField(verbose_name='xaydovchiPravaRaqami', max_length=200, null=True, blank=True)
    tartibRaqami = models.CharField(verbose_name='tartibRaqami', max_length=200, null=True, blank=True)
    tuzilganVaqti = models.CharField(verbose_name='tuzilganVaqti', max_length=200, null=True, blank=True)
    avtomobilTuri = models.CharField(verbose_name='avtomobilTuri', max_length=200, null=True, blank=True)
    avtomobilGosNomeri = models.CharField(verbose_name='avtomobilGosNomeri', max_length=200, null=True, blank=True)
    avtoKimniIxtiyorida = models.CharField(verbose_name='avtoKimniIxtiyorida', max_length=200, null=True, blank=True)
    jonashManzili = models.CharField(verbose_name='jonashManzili', max_length=200, null=True, blank=True)
    garajdanChiqishVaqti = models.CharField(verbose_name='garajdanChiqishVaqti', max_length=200, null=True, blank=True)
    garajdanChiqishVaqtiTasdiqlashFIO = models.CharField(verbose_name='garajdanChiqishVaqtiTasdiqlashFIO',
                                                         max_length=200, null=True, blank=True)
    garajgaQaytishVaqti = models.CharField(verbose_name='garajgaQaytishVaqti', max_length=200, blank=True, null=True)
    garajgaQaytishVaqtiTasdiqlashFIO = models.CharField(verbose_name='garajgaQaytishVaqtiTasdiqlashFIO', max_length=200,
                                                        blank=True, null=True)
    garajgaQaytishVaqtiTasdiqlandi = models.BooleanField(verbose_name='garajgaQaytishVaqtiTasdiqlandi', null=True,
                                                         blank=True)
    kechikishlar = models.CharField(verbose_name='kechikishlar', max_length=200, blank=True, null=True)
    kechikishlarYozdiFIO = models.CharField(verbose_name='kechikishlarYozdiFIO', max_length=200, blank=True, null=True)
    kechikishlarYozdiVaqti = models.CharField(verbose_name='kechikishlarYozdiVaqti', max_length=200, blank=True,
                                              null=True)
    avtoTexSozVaqti = models.CharField(verbose_name='avtoTexSozVaqti', max_length=200, blank=True, null=True)
    avtoTexSozTasdiqlashFIO = models.CharField(verbose_name='avtoTexSozTasdiqlashFIO', max_length=200, blank=True,
                                               null=True)
    avtoTexSozTasdiqlandi = models.BooleanField(verbose_name='avtoTexSozTasdiqlandi', null=True, blank=True)
    spidometrKorsatgichi = models.CharField(verbose_name='spidometrKorsatgichi', max_length=200, null=True, blank=True)
    spidometrYozdiFIO = models.CharField(verbose_name='spidometrYozdiFIO', max_length=200, null=True, blank=True)
    spidometrYozdiVaqti = models.CharField(verbose_name='spidometrYozdiVaqti', max_length=200, null=True, blank=True)
    chiqishgaRuxsatBerildi = models.BooleanField(verbose_name='chiqishgaRuxsatBerildi', null=True, blank=True)
    chiqishgaRuxsatBerdiFIO = models.CharField(verbose_name='chiqishgaRuxsatBerdiFIO', max_length=200, null=True,
                                               blank=True)
    chiqishgaRuxsatBerdiVaqti = models.CharField(verbose_name='chiqishgaRuxsatBerdiVaqti', max_length=200, null=True,
                                                 blank=True)
    xaydovchiSozXoldaQabulQildi = models.BooleanField(verbose_name='xaydovchiSozXoldaQabulQildi', null=True, blank=True)
    xaydovchiSozXoldaQabulQildiFIO = models.CharField(verbose_name='xaydovchiSozXoldaQabulQildiFIO', max_length=200,
                                                      null=True, blank=True)
    xaydovchiSozXoldaQabulQildiVaqti = models.CharField(verbose_name='xaydovchiSozXoldaQabulQildiVaqti', max_length=200,
                                                        null=True, blank=True)
    yoqilgiTuri = models.CharField(verbose_name='yoqilgiTuri', max_length=200, null=True, blank=True)
    yoqilgiQoldigiLitr = models.CharField(verbose_name='yoqilgiQoldigiLitr', max_length=200, null=True, blank=True)
    yoqilgiQoldigiYozdiFIO = models.CharField(verbose_name='yoqilgiQoldigiYozdiFIO', max_length=200, null=True,
                                              blank=True)
    yoqilgiQoldigiYozildiVaqti = models.CharField(verbose_name='yoqilgiQoldigiYozildiVaqti', max_length=200, null=True,
                                                  blank=True)
    yoqilgiQuyildiLitr = models.CharField(verbose_name='yoqilgiQuyildiLitr', max_length=200, null=True, blank=True)
    yoqilgiQuydiZapravshikFIO = models.CharField(verbose_name='yoqilgiQuydiZapravshikFIO', max_length=200, null=True,
                                                 blank=True)
    yoqilgiQuydiZapravshikVaqti = models.CharField(verbose_name='yoqilgiQuydiZapravshikVaqti', max_length=200,
                                                   null=True, blank=True)
    yoqilgiQuydiZapravshikTasdiqladi = models.BooleanField(verbose_name='yoqilgiQuydiZapravshikTasdiqladi', null=True,
                                                           blank=True)
    yoqilgiQuydiXaydovchiFIO = models.CharField(verbose_name='yoqilgiQuydiXaydovchiFIO', max_length=200, blank=True,
                                                null=True)
    yoqilgiQuydiXaydovchiVaqti = models.CharField(verbose_name='yoqilgiQuydiXaydovchiVaqti', max_length=200, blank=True,
                                                  null=True)
    yoqilgiQuydiXaydovchiTasdiqladi = models.BooleanField(verbose_name='yoqilgiQuydiXaydovchiTasdiqladi', null=True,
                                                          blank=True)
    yoqilgiSarfiLitr = models.CharField(verbose_name='yoqilgiSarfiLitr', blank=True, null=True, max_length=200)
    yoqilgiSarfiFIO = models.CharField(verbose_name='yoqilgiSarfiFIO', blank=True, null=True, max_length=200)
    yoqilgiSarfiVaqti = models.CharField(verbose_name='yoqilgiSarfiVaqti', blank=True, null=True, max_length=200)
    yoqilgiOxiridaQoldigiLitr = models.CharField(verbose_name='yoqilgiOxiridaQoldigiLitr', blank=True, null=True,
                                                 max_length=200)
    yoqilgiOxiridaQoldigiYozdiFIO = models.CharField(verbose_name='yoqilgiOxiridaQoldigiYozdiFIO', blank=True,
                                                     null=True, max_length=200)
    yoqilgiOxiridaQoldigiYozildiVaqti = models.CharField(verbose_name='yoqilgiOxiridaQoldigiYozildiVaqti', blank=True,
                                                         null=True, max_length=200)
    spidometrOxiridaKorsatgichi = models.CharField(verbose_name='spidometrOxiridaKorsatgichi', blank=True, null=True,
                                                   max_length=200)
    spidometrOxiridaYozdiFIO = models.CharField(verbose_name='spidometrOxiridaYozdiFIO', blank=True, null=True,
                                                max_length=200)
    spidometrOxiridaYozdiVaqti = models.CharField(verbose_name='spidometrOxiridaYozdiVaqti', blank=True, null=True,
                                                  max_length=200)
    avtoQabulQildiMexanikFIO = models.CharField(verbose_name='avtoQabulQildiMexanikFIO', blank=True, null=True,
                                                max_length=200)
    avtoQabulQildiMexanikVaqti = models.CharField(verbose_name='avtoQabulQildiMexanikVaqti', blank=True, null=True,
                                                  max_length=200)
    avtoQabulQildiMexanikTasdiqladi = models.BooleanField(verbose_name='avtoQabulQildiMexanikTasdiqladi', null=True,
                                                          blank=True)
    avtoQabulQildiXaydovchiFIO = models.CharField(verbose_name='avtoQabulQildiXaydovchiFIO', max_length=200, null=True,
                                                  blank=True)
    avtoQabulQildiXaydovchiVaqti = models.CharField(verbose_name='avtoQabulQildiXaydovchiVaqti', max_length=200,
                                                    null=True, blank=True)
    avtoQabulQildiXaydovchiTasdiqladi = models.BooleanField(verbose_name='avtoQabulQildiXaydovchiTasdiqladi', null=True,
                                                            blank=True)
    yopdiFIO = models.CharField(verbose_name='yopdiFIO', max_length=200, null=True, blank=True)
    yopilganVaqti = models.CharField(verbose_name='yopilganVaqti', max_length=200, null=True, blank=True)
    yopildiBool = models.BooleanField(verbose_name='yopildiBool', null=True, blank=True)
    yoqilgiQuyishVaraqasi = models.CharField(verbose_name='yoqilgiQuyishVaraqasi', max_length=200, null=True,
                                             blank=True)

    yoqilgiQuyishVaraqasi = models.CharField(verbose_name='yoqilgiQuyishVaraqasi', null=True, blank=True,
                                             max_length=200)
    yoqilgiMeyoriIndexsi = models.CharField(verbose_name='yoqilgiMeyoriIndexsi', null=True, blank=True, max_length=200)
    yoqilgiSarfiLitrMeyorBoyicha = models.CharField(verbose_name='yoqilgiSarfiLitrMeyorBoyicha', null=True, blank=True,
                                                    max_length=200)
    yoqilgiSarfiLitrAsl = models.CharField(verbose_name='yoqilgiSarfiLitrAsl', null=True, blank=True, max_length=200)
    yoqilgiTejaldi = models.CharField(verbose_name='yoqilgiTejaldi', null=True, blank=True, max_length=200)
    yoqilgiOrtiqchaSarf = models.CharField(verbose_name='yoqilgiOrtiqchaSarf', null=True, blank=True, max_length=200)
    topshiriwgaJamiKetganVaqt = models.CharField(verbose_name='topshiriwgaJamiKetganVaqt', null=True, blank=True,
                                                 max_length=200)

    class Meta:
        verbose_name = 'PutevoyList'
        verbose_name_plural = 'PutevoyList'


class BajarilganIshlar(models.Model):
    putevoy = models.ForeignKey(PutevoyList, on_delete=models.CASCADE, null=True, blank=True)
    tartibRaqami = models.CharField(verbose_name='tartibRaqami', max_length=200, null=True, blank=True)
    jonashManzili = models.CharField(verbose_name='jonashManzili', max_length=200, null=True, blank=True)
    jonashVaqti = models.CharField(verbose_name='jonashVaqti', max_length=200, null=True, blank=True)
    tugashManzili = models.CharField(verbose_name='tugashManzili', max_length=200, null=True, blank=True)
    tugashVaqti = models.CharField(verbose_name='tugashVaqti', max_length=200, null=True, blank=True)
    yolKM = models.CharField(verbose_name='yolKM', max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = 'BajarilganIshlar'
        verbose_name_plural = 'BajarilganIshlar'