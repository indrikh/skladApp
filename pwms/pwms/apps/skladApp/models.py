from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


import datetime

class Proizvodstvo(models.Model):
    adress = models.CharField(max_length=150)

    def __str__(self):
        return self.adress

class Sklad(models.Model):
    adress = models.CharField( max_length=150)
    square = models.FloatField()

class Stanok(models.Model):
    name = models.CharField( max_length=50)
    type = models.IntegerField()
    start_date = models.DateField( default=datetime.date.today)
    end_date = models.DateField(default=datetime.date.today)
    lifetime = models.IntegerField()
    proizvodstvo = models.ForeignKey(Proizvodstvo, on_delete=models.CASCADE)

class Detal(models.Model):
    number = models.IntegerField()
    name = models.CharField( max_length=100)
    stanok = models.ForeignKey(Stanok, on_delete=models.CASCADE)
    sklad = models.ForeignKey(Sklad, on_delete=models.CASCADE)

class systemUser(models.Model):
    user_base = models.ForeignKey(User, default=1 ,on_delete=models.CASCADE)
    username = models.CharField(max_length=25, blank=True)
    number = models.IntegerField()
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    password = models.CharField( max_length=150)
    birhtday = models.DateField(default=datetime.date.today)
    position = models.CharField( max_length=150)
    contact_number = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Nakladnaya(models.Model):
    sklad = models.ForeignKey(Sklad, on_delete=models.CASCADE)
    detal_number = models.IntegerField()
    detal_name = models.CharField( max_length=100)
    remontnik = models.ForeignKey(systemUser, on_delete=models.CASCADE)
    recive_date = models.DateField(default=datetime.date.today)
    price = models.FloatField()

    def __str__(self):
        return str(self.pk) + "_" + str(self.detal_number) + "_" + str(self.detal_name)

class Dbbackup(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=150)
    date = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return str(self.number) + "_" + str(self.name) + "_" + str(self.date)


class SkladAdmin(models.Model):
    user = models.ForeignKey(systemUser, on_delete=models.CASCADE)

class Rabotnik(models.Model):
    user = models.ForeignKey(systemUser, on_delete=models.CASCADE)
    order_sum = models.IntegerField(blank=True)
    last_order = models.ForeignKey(Nakladnaya, on_delete=models.CASCADE, blank=True, null=True)

    def add_order(self, nakl):
        self.order_sum += 1
        self.last_order = nakl

class Administrator(models.Model):
    user = models.ForeignKey(systemUser, on_delete=models.CASCADE)
    dbbackup_sum = models.IntegerField(null = True, default=1)
    dbbackup_last = models.ForeignKey(Dbbackup, on_delete=models.CASCADE, null=True, blank=True)

    def add_dbbackup(self, db):
        self.dbbackup_sum += 1
        self.dbbackup_last = db




