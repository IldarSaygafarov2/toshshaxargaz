from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Custom user model."""
    mobile_info = models.CharField(max_length=100, verbose_name='Mobile info', null=True, blank=True)
    version = models.CharField(max_length=100, verbose_name='Version', null=True, blank=True)
    post = models.CharField(max_length=100, verbose_name='Должность', null=True, blank=True)
    organization = models.CharField(max_length=100, verbose_name='Организация', null=True, blank=True)
    phone_number = models.CharField(max_length=15, verbose_name='Номер телефона', null=True, blank=True)
    buun = models.BooleanField(null=True, blank=True)
    login_check = models.BooleanField(null=True, blank=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class MobileInfo2(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    key = models.CharField(max_length=100, verbose_name='Ключ', null=True, blank=True)
    value = models.CharField(max_length=100, verbose_name='Значение', null=True, blank=True)

    def __str__(self):
        return f'{self.key}-{self.value}'

    class Meta:
        verbose_name = 'Мобильные данные'
        verbose_name_plural = 'Мобильные данные'


class UserPassport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Юзер', null=True, blank=True)
    last_name = models.CharField(max_length=100, verbose_name='Фамилия', null=True, blank=True)
    first_name = models.CharField(max_length=100, verbose_name='Имя', null=True, blank=True)
    surname = models.CharField(max_length=100, verbose_name='Отчество', null=True, blank=True)
    birth_date = models.DateField(verbose_name='Дата рождения', null=True, blank=True)
    issue_date = models.DateField(verbose_name='Дата выдачи', null=True, blank=True)
    expiration_date = models.DateField(verbose_name='Дата истечения срока', null=True, blank=True)
    sex = models.CharField(max_length=10, verbose_name='Пол', null=True, blank=True)
    citizenship = models.CharField(max_length=50, verbose_name='Гражданство', null=True, blank=True)
    passport_seria = models.CharField(max_length=20, verbose_name='Серия пасспорта', null=True, blank=True)
    personal_number = models.CharField(max_length=20, verbose_name='Личный номер', null=True, blank=True)
    birth_place = models.CharField(max_length=30, verbose_name='Место рождения', null=True, blank=True)
    residential_address = models.CharField(max_length=30, verbose_name='Адрес проживания', null=True, blank=True)

    class Meta:
        verbose_name = "Данные паспорта"
        verbose_name_plural = 'Данные паспорта'


class UserDriverLicense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', null=True, blank=True)
    date_of_issue = models.DateField(verbose_name='Дата выдачи', null=True, blank=True)
    expiration_date = models.DateField(verbose_name='Дата окончания срока', null=True, blank=True)
    place_of_issue = models.CharField(max_length=100, verbose_name='Место выдачи', null=True, blank=True)
    testimonial_number = models.CharField(verbose_name='Номер свидетельства', max_length=50, null=True, blank=True)
    category = models.CharField(max_length=10, verbose_name='Категория', null=True, blank=True)
    characters = models.CharField(max_length=50, verbose_name='Персонажи', null=True, blank=True)

    class Meta:
        verbose_name = 'Права'
        verbose_name_plural = 'Права'


class UserAdditionalData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', null=True, blank=True)
    work_time = models.CharField(max_length=50, verbose_name='Время работы', null=True, blank=True)
    end_time = models.CharField(max_length=50, verbose_name='Время выхода', null=True, blank=True)
    order_time = models.CharField(max_length=50, verbose_name='Введеный номер заказа', null=True, blank=True)
    experience = models.CharField(max_length=50, verbose_name='Стаж', null=True, blank=True)
    dismissed_order_number = models.CharField(max_length=50, verbose_name='Номер отклоненного заказа', null=True, blank=True)
    characters = models.CharField(max_length=50, verbose_name='Отдельные персонажи', null=True, blank=True)

    class Meta:
        verbose_name = 'Дополнительные данные'
        verbose_name_plural = 'Дополнительные данные'


class Employee(models.Model):
    last_name = models.CharField(max_length=50, verbose_name='Фамилия', null=True, blank=True)
    name = models.CharField(max_length=50, verbose_name='Имя', null=True, blank=True)
    surname = models.CharField(max_length=40, verbose_name='Отчество', null=True, blank=True)
    position = models.CharField(max_length=50, verbose_name='Позиция', null=True, blank=True)
    position_key = models.CharField(max_length=40, verbose_name='Ключ позиции', null=True, blank=True)
    specialty = models.CharField(max_length=30, verbose_name='Специальность', null=True, blank=True)
    organization = models.CharField(max_length=40, verbose_name='Организация', null=True, blank=True)
    phone_number = models.CharField(verbose_name='Номер телефона', max_length=15, null=True, blank=True)

    class Meta:
        verbose_name = 'Рабочий'
        verbose_name_plural = 'Рабочие'
