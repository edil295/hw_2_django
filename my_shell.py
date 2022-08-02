from credit.models import Client, Account, Credit
from random import randint


def chislo():
    num = randint(1000000000000000, 9999999999999999)
    return num


def suda():
    num = randint(10000, 100000)
    return num


c1 = Client(name='Бердиев Н.Д', citizenship='КР', birth_day='1994-11-09', work_place='Codify')
c1.save()
c2 = Client(name='Примкулов Э.К', citizenship='КЗ', birth_day='1999-05-29', work_place='Скорая помощь')
c2.save()

a1 = Account(number=chislo(), client=c1)
a2 = Account(number=chislo(), client=c1)
a3 = Account(number=chislo(), client=c2)
a4 = Account(number=chislo(), client=c2)
a1.save()
a2.save()
a3.save()
a4.save()

k1 = Credit(sum=suda(), account=a1)
k2 = Credit(sum=suda(), account=a2)
k3 = Credit(sum=suda(), account=a3)
k4 = Credit(sum=suda(), account=a4)