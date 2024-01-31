from django.contrib import admin
from . import models


class UserPassportInline(admin.StackedInline):
    model = models.UserPassport
    extra = 1


class UserAdditionalDataInline(admin.StackedInline):
    model = models.UserAdditionalData
    extra = 1


class UserDriverLicenseInline(admin.StackedInline):
    model = models.UserDriverLicense
    extra = 1


class MobileInfo2Inline(admin.StackedInline):
    model = models.MobileInfo2
    extra = 1


class UserAdmin(admin.ModelAdmin):
    inlines = [
        UserPassportInline,
        UserAdditionalDataInline,
        UserDriverLicenseInline,
        MobileInfo2Inline
    ]
    list_display = ('pk', 'username', 'first_name', 'last_name', 'email', 'password')
    list_display_links = ('pk', 'username')


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Employee)
