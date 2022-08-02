from django.db import models
from datetime import date


class Client(models.Model):
    name = models.CharField(max_length=20, verbose_name='ФИО клиента')
    citizenship = models.CharField(max_length=20, default='Кыргызстан', verbose_name='Гражданство')
    birth_day = models.DateField(verbose_name='Год рождения')
    work_place = models.CharField(max_length=30, blank=True, null=True, verbose_name='Место работы')
    update_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата обновление')

    def __str__(self):
        return f'{self.name} - {self.birth_day}'

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = 'Клиенты'
        db_table = 'customers'


class Account(models.Model):
    number = models.CharField(max_length=16, unique=True, verbose_name='Номер аккаунта')
    account_type = models.IntegerField(default=1, verbose_name='Тип аккаунта')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Клиент')

    def __str__(self):
        return f'{self.number}'

    class Meta:
        verbose_name = "Счет"
        verbose_name_plural = 'Счета'
        db_table = 'accounts'


class Credit(models.Model):
    sum = models.IntegerField('Cумма кредита')
    date = models.DateField(default=date.today(), verbose_name='Дата получение кредита')
    account = models.ForeignKey(Account, on_delete=models.CASCADE, verbose_name='Cчет')

    def __str__(self):
        return f'{self.sum}'

    class Meta:
        verbose_name = "Кредит"
        verbose_name_plural = 'Кредиты'
        db_table = 'loans'
