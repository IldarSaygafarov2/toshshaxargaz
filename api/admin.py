from django.contrib import admin
from .models import *


class AlmashtirilganZapchastRoyxatiInline(admin.StackedInline):
    model = AlmashtirilganZapchastRoyxati
    extra = 1


class AlmashtirilganZapchastRoyxatiInline2(admin.StackedInline):
    model = AlmashtirilganZapchastRoyxati2
    extra = 1


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    pass


@admin.register(TransportSketch)
class TransportSketchAdmin(admin.ModelAdmin):
    pass


@admin.register(TexnikKorik)
class TexnikKorikAdmin(admin.ModelAdmin):
    inlines = [AlmashtirilganZapchastRoyxatiInline]


@admin.register(Zapchast)
class ZapchastAdmin(admin.ModelAdmin):
    inlines = [AlmashtirilganZapchastRoyxatiInline2]


@admin.register(TSModeli)
class TSModeliAdmin(admin.ModelAdmin):
    pass


@admin.register(YoqilgiOstatkasi)
class YoqilgiOstatkasiAdmin(admin.ModelAdmin):
    pass


@admin.register(SpidometrKorsatgichi)
class SpidometrKorsatgichiAdmin(admin.ModelAdmin):
    pass


@admin.register(QoshimchaMalumotlar)
class QoshimchaMalumotlarAdmin(admin.ModelAdmin):
    pass


@admin.register(Test_Filiallar)
class Test_Filiallar_Admin(admin.ModelAdmin):
    pass


@admin.register(Test_Xodimlar)
class Test_Xodimlar_Admin(admin.ModelAdmin):
    pass


@admin.register(Test_Xaydovchilar)
class Test_Xaydovchilar_Admin(admin.ModelAdmin):
    pass


@admin.register(Test_Transport)
class Test_Transport_Admin(admin.ModelAdmin):
    pass


class BajarilganIshlarInline(admin.StackedInline):
    model = BajarilganIshlar
    extra = 1


@admin.register(PutevoyList)
class PutevoyListAdmin(admin.ModelAdmin):
    inlines = [BajarilganIshlarInline]


