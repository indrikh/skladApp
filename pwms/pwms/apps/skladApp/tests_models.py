from django.test import TestCase
import unittest
from .models import systemUser, Administrator, SkladAdmin, Rabotnik, Stanok, Sklad, Detal, Proizvodstvo, Nakladnaya, Dbbackup
import datetime
from django.contrib.auth.models import User


class systemUser_ModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user_base = User.objects.create_user(username="user", password="123")
        systemUser.objects.create(user_base=user_base, username="user", password="123", number=123, first_name="Иван", last_name="Иванов", birhtday=datetime.date.today, position="Склад", contact_number="1")

    def test_username_lable(self):
        ad = systemUser.objects.get(id=1)
        field_label = ad._meta.get_field('username').verbose_name
        self.assertEqual(field_label, 'username')

    def test_password_lable(self):
        ad = systemUser.objects.get(id=1)
        field_label = ad._meta.get_field('password').verbose_name
        self.assertEqual(field_label, 'password')

    def test_first_name_lable(self):
        ad = systemUser.objects.get(id=1)
        field_label = ad._meta.get_field('first_name').verbose_name
        self.assertEqual(field_label, 'first_name')

    def test_last_name_lable(self):
        ad = systemUser.objects.get(id=1)
        field_label = ad._meta.get_field('last_name').verbose_name
        self.assertEqual(field_label, 'last_name')

    def test_number_lable(self):
        ad = systemUser.objects.get(id=1)
        field_label = ad._meta.get_field('number').verbose_name
        self.assertEqual(field_label, 'number')

    def test_position_lable(self):
        ad = systemUser.objects.get(id=1)
        field_label = ad._meta.get_field('position').verbose_name
        self.assertEqual(field_label, 'position')

    def test_contact_number_lable(self):
        ad = systemUser.objects.get(id=1)
        field_label = ad._meta.get_field('contact_number').verbose_name
        self.assertEqual(field_label, 'contact_number')

    def test_birhtday_lable(self):
        ad = systemUser.objects.get(id=1)
        field_label = ad._meta.get_field('birhtday').verbose_name
        self.assertEqual(field_label, 'birhtday')

    def test_username_max_length(self):
        ad = systemUser.objects.get(id=1)
        field_label = ad._meta.get_field('username').max_length
        self.assertEqual(field_label, 'username')

    def test_password_max_legth(self):
        ad = systemUser.objects.get(id=1)
        field_label = ad._meta.get_field('password').max_length
        self.assertEqual(field_label, 'password')

    def test_first_name_max_legth(self):
        ad = systemUser.objects.get(id=1)
        field_label = ad._meta.get_field('first_name').max_legth
        self.assertEqual(field_label, 'first_name')

    def test_last_name_max_legth(self):
        ad = systemUser.objects.get(id=1)
        field_label = ad._meta.get_field('last_name').max_legth
        self.assertEqual(field_label, 'last_name')

    def test_number_max_legth(self):
        ad = systemUser.objects.get(id=1)
        field_label = ad._meta.get_field('number').max_legth
        self.assertEqual(field_label, 'number')

    def test_position_max_legth(self):
        ad = systemUser.objects.get(id=1)
        field_label = ad._meta.get_field('position').max_legth
        self.assertEqual(field_label, 'position')

    def test_contact_number_max_legth(self):
        ad = systemUser.objects.get(id=1)
        field_label = ad._meta.get_field('contact_number').max_legth
        self.assertEqual(field_label, 'contact_number')

    def test_birhtday_max_legth(self):
        ad = systemUser.objects.get(id=1)
        field_label = ad._meta.get_field('birhtday').max_legth
        self.assertEqual(field_label, 'birhtday')

class SkladAdmin_ModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user_base = User.objects.create_user(username="user", password="123")
        sys_user = systemUser.objects.create(user_base=user_base, username="user", password="123", number=123, first_name="Иван", last_name="Иванов", birhtday=datetime.date.today, position="Склад", contact_number="1")
        SkladAdmin.objects.create(user=sys_user)

class Administrator_ModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user_base = User.objects.create_user(username="user", password="123")
        sys_user = systemUser.objects.create(user_base=user_base, username="user", password="123", number=123,
                                             first_name="Иван", last_name="Иванов", birhtday=datetime.date.today,
                                             position="Склад", contact_number="1")
        Administrator.objects.create(user = sys_user)

    def test_order_sum_lable(self):
        ad = Administrator.objects.get(id=1)
        field_label = ad._meta.get_field('dbbackup_sum').verbose_name
        self.assertEqual(field_label, 'dbbackup_sum')

    def test_order_sum_legth(self):
        ad = Administrator.objects.get(id=1)
        field_label = ad._meta.get_field('dbbackup_sum').max_legth
        self.assertEqual(field_label, 'dbbackup_sum')

class Dbbackup_ModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Dbbackup.objects.create(number = 1, name = "auto", date=datetime.date.today)

    def test_number_lable(self):
        ad = Dbbackup.objects.get(id=1)
        field_label = ad._meta.get_field('number').verbose_name
        self.assertEqual(field_label, 'number')

    def test_number_legth(self):
        ad = Dbbackup.objects.get(id=1)
        field_label = ad._meta.get_field('number').max_legth
        self.assertEqual(field_label, 'number')

    def test_name_lable(self):
        ad = Dbbackup.objects.get(id=1)
        field_label = ad._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_name_legth(self):
        ad = Dbbackup.objects.get(id=1)
        field_label = ad._meta.get_field('name').max_legth
        self.assertEqual(field_label, 'name')

    def test_date_lable(self):
        ad = Dbbackup.objects.get(id=1)
        field_label = ad._meta.get_field('date').verbose_name
        self.assertEqual(field_label, 'date')

    def test_date_legth(self):
        ad = Dbbackup.objects.get(id=1)
        field_label = ad._meta.get_field('date').max_legth
        self.assertEqual(field_label, 'date')

class Rabotnik_ModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user_base = User.objects.create_user(username="user", password="123")
        sys_user = systemUser.objects.create(user_base=user_base, username="user", password="123", number=123,
                                             first_name="Иван", last_name="Иванов", birhtday=datetime.date.today,
                                             position="Склад", contact_number="1")
        Rabotnik.objects.create(user=sys_user)

    def test_order_sum_lable(self):
        ad = Rabotnik.objects.get(id=1)
        field_label = ad._meta.get_field('order_sum').verbose_name
        self.assertEqual(field_label, 'order_sum')

    def test_order_sum_legth(self):
        ad = Rabotnik.objects.get(id=1)
        field_label = ad._meta.get_field('order_sum').max_legth
        self.assertEqual(field_label, 'order_sum')

class Proizvodstvo_ModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Proizvodstvo.objects.create(adress = "Адрес")

    def test_adress_lable(self):
        ad = Proizvodstvo.objects.get(id=1)
        field_label = ad._meta.get_field('adress').verbose_name
        self.assertEqual(field_label, 'adress')

    def test_adress_legth(self):
        ad = Proizvodstvo.objects.get(id=1)
        field_label = ad._meta.get_field('adress').max_legth
        self.assertEqual(field_label, 'adress')

class Sklad_ModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Sklad.objects.create(adress="Адрес", square=1.5)

    def test_adress_lable(self):
        ad = Sklad.objects.get(id=1)
        field_label = ad._meta.get_field('adress').verbose_name
        self.assertEqual(field_label, 'adress')

    def test_adress_legth(self):
        ad = Sklad.objects.get(id=1)
        field_label = ad._meta.get_field('adress').max_legth
        self.assertEqual(field_label, 'adress')

    def test_square_lable(self):
        ad = Sklad.objects.get(id=1)
        field_label = ad._meta.get_field('square').verbose_name
        self.assertEqual(field_label, 'square')

    def test_square_legth(self):
        ad = Sklad.objects.get(id=1)
        field_label = ad._meta.get_field('square').max_legth
        self.assertEqual(field_label, 'square')

class Detal_ModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        stanok = Stanok.objects.create(name = "Станок фрезерный", type = 1, start_date=datetime.date.today, end_date=datetime.date.today, proizvodstvo = Proizvodstvo.objects.create(adress = "Адрес"))
        sklad = Sklad.objects.create(adress="Адрес", square=1.5)
        Detal.objects.create(number=1, name="Фрезер", stanok = stanok, sklad=sklad)

    def test_number_lable(self):
        ad = Detal.objects.get(id=1)
        field_label = ad._meta.get_field('number').verbose_name
        self.assertEqual(field_label, 'number')

    def test_number_legth(self):
        ad = Detal.objects.get(id=1)
        field_label = ad._meta.get_field('number').max_legth
        self.assertEqual(field_label, 'number')

    def test_name_lable(self):
        ad = Detal.objects.get(id=1)
        field_label = ad._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_name_legth(self):
        ad = Detal.objects.get(id=1)
        field_label = ad._meta.get_field('name').max_legth
        self.assertEqual(field_label, 'name')

class Stanok_ModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Stanok.objects.create(name = "Станок фрезерный", type = 1, start_date=datetime.date.today, end_date=datetime.date.today, proizvodstvo = Proizvodstvo.objects.create(adress = "Адрес"))

    def test_name_lable(self):
        ad = Stanok.objects.get(id=1)
        field_label = ad._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_name_legth(self):
        ad = Stanok.objects.get(id=1)
        field_label = ad._meta.get_field('name').max_legth
        self.assertEqual(field_label, 'name')

    def test_type_lable(self):
        ad = Stanok.objects.get(id=1)
        field_label = ad._meta.get_field('type').verbose_name
        self.assertEqual(field_label, 'type')

    def test_type_legth(self):
        ad = Stanok.objects.get(id=1)
        field_label = ad._meta.get_field('type').max_legth
        self.assertEqual(field_label, 'type')

    def test_start_date_lable(self):
        ad = Stanok.objects.get(id=1)
        field_label = ad._meta.get_field('start_date').verbose_name
        self.assertEqual(field_label, 'start_date')

    def test_start_date_legth(self):
        ad = Stanok.objects.get(id=1)
        field_label = ad._meta.get_field('start_date').max_legth
        self.assertEqual(field_label, 'start_date')

    def test_end_date_lable(self):
        ad = Stanok.objects.get(id=1)
        field_label = ad._meta.get_field('end_date').verbose_name
        self.assertEqual(field_label, 'end_date')

    def test_end_date_legth(self):
        ad = Stanok.objects.get(id=1)
        field_label = ad._meta.get_field('end_date').max_legth
        self.assertEqual(field_label, 'end_date')

    def test_lifetime_lable(self):
        ad = Stanok.objects.get(id=1)
        field_label = ad._meta.get_field('lifetime').verbose_name
        self.assertEqual(field_label, 'lifetime')

    def test_lifetime_legth(self):
        ad = Stanok.objects.get(id=1)
        field_label = ad._meta.get_field('lifetime').max_legth
        self.assertEqual(field_label, 'lifetime')

class Nakladnaya_ModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        sklad = Sklad.objects.create(adress="Адрес", square=1.5)
        user_base = User.objects.create_user(username="user", password="123")
        sys_user = systemUser.objects.create(user_base=user_base, username="user", password="123", number=123,
                                             first_name="Иван", last_name="Иванов", birhtday=datetime.date.today,
                                             position="Склад", contact_number="1")
        remontnik = Rabotnik.objects.create(user=sys_user)
        Nakladnaya.objects.create(sklad=sklad, detal_number=1, detal_name="Фрезер", remontnik=remontnik, recive_date = datetime.date.today, price=1.3)

    def test_detal_number_lable(self):
        ad = Nakladnaya.objects.get(id=1)
        field_label = ad._meta.get_field('detal_number').verbose_name
        self.assertEqual(field_label, 'detal_number')

    def test_detal_number_legth(self):
        ad = Nakladnaya.objects.get(id=1)
        field_label = ad._meta.get_field('detal_number').max_legth
        self.assertEqual(field_label, 'detal_number')

    def test_detal_name_lable(self):
        ad = Nakladnaya.objects.get(id=1)
        field_label = ad._meta.get_field('detal_name').verbose_name
        self.assertEqual(field_label, 'detal_name')

    def test_detal_name_legth(self):
        ad = Nakladnaya.objects.get(id=1)
        field_label = ad._meta.get_field('detal_name').max_legth
        self.assertEqual(field_label, 'detal_name')

    def test_recive_date_lable(self):
        ad = Nakladnaya.objects.get(id=1)
        field_label = ad._meta.get_field('recive_date').verbose_name
        self.assertEqual(field_label, 'recive_date')

    def test_recive_date_legth(self):
        ad = Nakladnaya.objects.get(id=1)
        field_label = ad._meta.get_field('recive_date').max_legth
        self.assertEqual(field_label, 'recive_date')

    def test_price_lable(self):
        ad = Nakladnaya.objects.get(id=1)
        field_label = ad._meta.get_field('price').verbose_name
        self.assertEqual(field_label, 'price')

    def test_price_legth(self):
        ad = Nakladnaya.objects.get(id=1)
        field_label = ad._meta.get_field('price').max_legth
        self.assertEqual(field_label, 'price')