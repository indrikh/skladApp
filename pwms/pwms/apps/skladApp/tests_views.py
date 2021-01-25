from django.test import TestCase
import unittest
from .models import systemUser, Administrator, SkladAdmin, Rabotnik, Stanok, Sklad, Detal, Proizvodstvo, Nakladnaya, Dbbackup
from django.urls import reverse
from django.contrib.auth.models import User
import datetime

class View_Sklad_Test(TestCase):
    @classmethod
    def setUpTestData(cls):
        user_base = User.objects.create_user(username="user", password="123")
        Sklad.objects.create(adress="Адрес", square=1.5)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('sklad/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('skladIndex'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('skladIndex'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'skladApp/skladDataTable.html')

class View_Proizvodstvo_Test(TestCase):
    @classmethod
    def setUpTestData(cls):
        user_base = User.objects.create_user(username="user", password="123")
        Proizvodstvo.objects.create(adress="Адрес")

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('proizv/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('proizvIndex'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('proizvIndex'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'skladApp/proizvodstvoDataTable.html')

class View_SkladAdmin_Test(TestCase):
    @classmethod
    def setUpTestData(cls):
        user_base = User.objects.create_user(username="user", password="123")
        sys_user = systemUser.objects.create(user_base=user_base, username="user", password="123", number=123,
                                             first_name="Иван", last_name="Иванов", birhtday=datetime.date.today,
                                             position="Склад", contact_number="1")
        SkladAdmin.objects.create(user=sys_user)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('skladAdminMenu/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('skladAdminIndex'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('skladAdminIndex'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'skladApp/skladAdminMenu.html')

class View_Administrator_Test(TestCase):
    @classmethod
    def setUpTestData(cls):
        user_base = User.objects.create_user(username="user", password="123")
        sys_user = systemUser.objects.create(user_base=user_base, username="user", password="123", number=123,
                                             first_name="Иван", last_name="Иванов", birhtday=datetime.date.today,
                                             position="Склад", contact_number="1")
        Administrator.objects.create(user=sys_user)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('systemAdminMenu/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('systemAdminIndex'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('systemAdminIndex'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'skladApp/userAdminMenu.html')

class View_Dbbackup_Test(TestCase):
    @classmethod
    def setUpTestData(cls):
        Dbbackup.objects.create(number=1, name="auto", date=datetime.date.today)
        user_base = User.objects.create_user(username="user", password="123")

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('systemAdminMenu/Dbbackup/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('dbbackupIndex'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('dbbackupIndex'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'skladApp/dbdackupDataTable.html')

class View_Rabotnik_Test(TestCase):
    @classmethod
    def setUpTestData(cls):
        user_base = User.objects.create_user(username="user", password="123")
        sys_user = systemUser.objects.create(user_base=user_base, username="user", password="123", number=123,
                                             first_name="Иван", last_name="Иванов", birhtday=datetime.date.today,
                                             position="Склад", contact_number="1")
        Rabotnik.objects.create(user=sys_user)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('systemAdminMenu/rabotnikUsers/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('remontnikUserDataIndex'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('remontnikUserDataIndex'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'skladApp/remontnikUserDataTable.html')

class View_Detal_Test(TestCase):
    @classmethod
    def setUpTestData(cls):
        user_base = User.objects.create_user(username="user", password="123")
        stanok = Stanok.objects.create(name="Станок фрезерный", type=1, start_date=datetime.date.today,
                                       end_date=datetime.date.today,
                                       proizvodstvo=Proizvodstvo.objects.create(adress="Адрес"))
        sklad = Sklad.objects.create(adress="Адрес", square=1.5)
        Detal.objects.create(number=1, name="Фрезер", stanok=stanok, sklad=sklad)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('detals/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('detalIndex'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('detalIndex'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'skladApp/detalDataTable.html')

class View_Stanok_Test(TestCase):
    @classmethod
    def setUpTestData(cls):
        user_base = User.objects.create_user(username="user", password="123")
        Stanok.objects.create(name = "Станок фрезерный", type = 1, start_date=datetime.date.today, end_date=datetime.date.today, proizvodstvo = Proizvodstvo.objects.create(adress = "Адрес"))


    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('stanoks/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('stanokIndex'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('stanokIndex'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'skladApp/stanokDataTable.html')

class View_Nakladnaya_Test(TestCase):
    @classmethod
    def setUpTestData(cls):
        sklad = Sklad.objects.create(adress="Адрес", square=1.5)
        user_base = User.objects.create_user(username="user", password="123")
        sys_user = systemUser.objects.create(user_base=user_base, username="user", password="123", number=123,
                                             first_name="Иван", last_name="Иванов", birhtday=datetime.date.today,
                                             position="Склад", contact_number="1")
        remontnik = Rabotnik.objects.create(user=sys_user)
        Nakladnaya.objects.create(sklad=sklad, detal_number=1, detal_name="Фрезер", remontnik=remontnik,
                                  recive_date=datetime.date.today, price=1.3)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('rabotnikMenu/nakls/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('rabotnikNaklsIndex'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('rabotnikNaklsIndex'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'skladApp/naklViewTable.html')