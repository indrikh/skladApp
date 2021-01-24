from django.http import  HttpResponse, HttpResponseRedirect, Http404
from django.views import View
import datetime
from django.contrib import auth
from django.shortcuts import render
from .models import  Proizvodstvo, Sklad, Stanok, Detal, Nakladnaya,  Rabotnik, Administrator, SkladAdmin, systemUser, Dbbackup
from django.urls import reverse
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User, Permission


@login_required(login_url='authIndex')
def rabotnikIndex(request):
    if request.user.is_authenticated:
        d = Detal.objects.values()
        return render(request, 'skladApp/rabotnikMenu.html', {'detals': d})
    else:
        return HttpResponse("Вы не авторизованы!")

@login_required(login_url='authIndex')
def rabotnikNaklsIndex(request):
    user = User.objects.get(username = request.user.username)
    sys_user = systemUser.objects.get(user_base = user)
    #nakls = Nakladnaya.objects.values()
    nakls = Nakladnaya.objects.all().filter(remontnik=sys_user)
    res = []
    res.append("id")
    res.append("Склад")
    res.append("Номер детали")
    res.append("Название детали")
    res.append("Ремонтник")
    res.append("Дата получения")
    res.append("Цена")
    data = nakls
    return render(request, 'skladApp/naklViewTable.html', {'data_table' :data  , 'titles' : res})

@login_required(login_url='authIndex')
def AddNakl(requset):
    detal_id = requset.POST['detal']
    price = requset.POST['price']
    try:
        d = Detal.objects.get(id = detal_id)
    except:
        raise Http404("Нет детали")
    user = User.objects.get(username=requset.user.username)
    sys_user = systemUser.objects.get(user_base=user)
    n = Nakladnaya(sklad=d.sklad, detal_number=d.number, detal_name=d.name, remontnik=sys_user, price=price)
    n.save()
    rem = Rabotnik.objects.get(user = sys_user)
    rem.add_order(n)
    rem.save()
    d.delete()
    return HttpResponseRedirect(reverse('rabotnikIndex'))

@login_required(login_url='authIndex')
def skladAdminIndex(request):
    return render(request, 'skladApp/skladAdminMenu.html')

@login_required(login_url='authIndex')
def systemAdminIndex(request):
    return render(request, 'skladApp/userAdminMenu.html')

class stanok_view(View):
    @login_required(login_url='authIndex')
    def stanokIndex(request):
        adms = Stanok.objects.values()
        res = []
        res.append("id")
        res.append("Название")
        res.append("Тип")
        res.append("Начало эксплуатации")
        res.append("Конец эксплуатации")
        res.append("Лет эксплуатации")
        res.append("Производство")
        data = adms
        privodstva = Proizvodstvo.objects.all()

        return render(request, 'skladApp/stanokDataTable.html', {'data_table' :data  , 'titles' : res, 'proizvs': privodstva})
        #return HttpResponse(data)

    @login_required(login_url='authIndex')
    def StanoksAddData(request):
        name = request.POST['name']
        type = request.POST['type']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        lifetime = datetime.datetime.strptime(end_date, '%Y-%m-%d').year - datetime.datetime.strptime(start_date, '%Y-%m-%d').year
        proizvid = request.POST['proizv']
        try:
            p = Proizvodstvo.objects.get(id = proizvid)
        except:
            raise Http404("Производство не найдено")

        a = Stanok(name=name, type=type, start_date=start_date, end_date=end_date, lifetime=lifetime, proizvodstvo=p)
        a.save()
        return HttpResponseRedirect(reverse('stanokIndex'))
        #return HttpResponse(lifetime)

    @login_required(login_url='authIndex')
    def DeleteData(request):
        id = request.POST['remove_id']
        try:
            a = Stanok.objects.get( id = id )
        except:
            raise Http404("Запись не найдена")
        Stanok.objects.filter(id=id).delete()
        return HttpResponseRedirect(reverse('stanokIndex'))

    @login_required(login_url='authIndex')
    def UpdateStanoksData(request):
        id = request.POST['update_id']
        try:
            a = Stanok.objects.get( id = id)
        except:
            raise Http404("Неверный id")

        name = request.POST['name']
        type = request.POST['type']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        lifetime = datetime.datetime.strptime(end_date, '%Y-%m-%d').year - datetime.datetime.strptime(start_date, '%Y-%m-%d').year
        proizvid = request.POST['proizv']
        try:
            s = Proizvodstvo.objects.get(id = proizvid)
        except:
            raise Http404("Производство не найдено")
        a.name = name
        a.type = type
        a.start_date = start_date
        a.end_date = end_date
        a.lifetime = lifetime
        a.proizvodsvto = s
        a.save()
        return HttpResponseRedirect(reverse('stanokIndex'))

    @login_required(login_url='authIndex')
    def updateTable(request):
        return HttpResponseRedirect(reverse('stanokIndex'))

class detal_view(View):
    @login_required(login_url='authIndex')
    def detalIndex(request):
        dets = Detal.objects.values()
        res = []
        res.append("id")
        res.append("Номер")
        res.append("Название")
        res.append("Станок")
        res.append("Склад")
        data = list(dets)
        stanoks = Stanok.objects.all()
        sklads = Sklad.objects.all()
        #return HttpResponse(data)
        return render(request, 'skladApp/detalDataTable.html', {'data_table': data, 'titles': res, 'stanoks': stanoks, 'sklads':sklads})

    @login_required(login_url='authIndex')
    def RefreshDetalTable(request):
        return HttpResponseRedirect(reverse('detalIndex'))

    @login_required(login_url='authIndex')
    def DetalAddData(request):
        number = request.POST['number']
        name = request.POST['name']
        stanok = request.POST['stanok']
        sklad = request.POST['sklad']
        try:
            s = Stanok.objects.get(id = stanok)
            sk = Sklad.objects.get(id = sklad)
        except:
            raise Http404("Производство не найдено")
        a = Detal(number=number, name=name,stanok=s, sklad=sk)
        a.save()
        return HttpResponseRedirect(reverse('detalIndex'))

    @login_required(login_url='authIndex')
    def DetalDeleteData(request):
        id = request.POST['remove_id']
        try:
            a = Detal.objects.get(id=id)
        except:
            raise Http404("Запись не найдена")
        Detal.objects.filter(id=id).delete()
        return HttpResponseRedirect(reverse('detalIndex'))

    @login_required(login_url='authIndex')
    def DetalUpdateData(request):
        id = request.POST['update_id']
        try:
            a = Detal.objects.get( id = id)
        except:
            raise Http404("Неверный id")
        number = request.POST['number']
        name = request.POST['name']
        stanok = request.POST['stanok']
        sklad = request.POST['sklad']
        try:
            s = Stanok.objects.get(id = stanok)
            sk = Sklad.objects.get(id = sklad)
        except:
            raise Http404("Производство не найдено")
        a.number = number
        a.name = name
        a.stanok = s
        a.sklad = sk
        a.save()
        return HttpResponseRedirect(reverse('detalIndex'))

class skladAdmin_view(View):
    @login_required(login_url='authIndex')
    def skladUserIndex(request):
        users = systemUser.objects.all().filter(position="Склад")
        # users = systemUser.objects.values()
        res = []
        res.append("id")
        res.append("Номер")
        res.append("Логин")
        res.append("Имя")
        res.append("Фамилия")
        res.append("Пароль")
        res.append("Дата рождения")
        res.append("Телефон")
        data = users
        return render(request, 'skladApp/skladUserDataTable.html', {'data_table': data, 'titles': res})

    @login_required(login_url='authIndex')
    def SkladUserAddData(request):
        number = request.POST['number']
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        birthday = request.POST['birthday']
        contact_number = request.POST['contact_number']
        base_user = User(username=username, password = make_password(password))
        base_user.save()
        base_user = User.objects.get(username=username)
        user = systemUser(user_base=base_user, number=number, username=username, first_name=first_name, last_name=last_name, password=password, position="Склад", birhtday=birthday, contact_number=contact_number)
        user.save()
        user = systemUser.objects.get(username = username)
        sklad_user = SkladAdmin(user=user)
        sklad_user.save()
        return HttpResponseRedirect(reverse('skladUserDataIndex'))

    @login_required(login_url='authIndex')
    def SkladDeleteUserData(request):
        id = request.POST['remove_id']
        try:
            a = systemUser.objects.get( id = id )
        except:
            raise Http404("Запись не найдена")
        SkladAdmin.objects.get(user=a).delete()
        user_base = a.user_base
        systemUser.objects.filter(id=id).delete()
        user_base.delete()
        a.delete()
        return HttpResponseRedirect(reverse('skladUserDataIndex'))

    @login_required(login_url='authIndex')
    def SkladUserUpdateData(request):
        id = request.POST['update_id']
        try:
            a = systemUser.objects.get(id=id)
        except:
            raise Http404("Неверный id")

        number = request.POST['number']
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        birthday = request.POST['birthday']
        contact_number = request.POST['contact_number']
        a.number = number
        a.username = username
        a.first_name = first_name
        a.last_name = last_name
        a.password = password
        a.birhtday = birthday
        a.contact_number = contact_number
        a.user_base.username = username
        a.user_base.password = make_password(password)
        a.user_base.save()
        a.save()
        return HttpResponseRedirect(reverse('skladUserDataIndex'))

class remontnikUser_view(View):
    @login_required(login_url='authIndex')
    def remontnikUserIndex(request):
        #users = systemUser.objects.all().filter(position="Работник")
        users = systemUser.objects.values().filter(position="Работник")
        res = []
        res.append("id")
        res.append("Номер")
        res.append("Логин")
        res.append("Имя")
        res.append("Фамилия")
        res.append("Пароль")
        res.append("Дата рождения")
        res.append("Телефон")
        res.append("Количество заказов")
        res.append("Последний заказ")
        data = list(users)
        for item in data:
            rab = Rabotnik.objects.get(user_id = item['id'])
            item['sum'] = rab.order_sum
            item['last'] = rab.last_order
        return render(request, 'skladApp/remontnikUserDataTable.html', {'data_table': data, 'titles': res})
        #return HttpResponse(data)

    @login_required(login_url='authIndex')
    def remontnikUserAddData(request):
        number = request.POST['number']
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        birthday = request.POST['birthday']
        contact_number = request.POST['contact_number']
        order_sum = 0
        base_user = User(username=username, password = make_password(password))
        base_user.save()
        base_user = User.objects.get(username=username)
        user = systemUser(user_base=base_user, number=number, username=username, first_name=first_name, last_name=last_name, password=password, position="Работник", birhtday=birthday, contact_number=contact_number)
        user.save()
        user = systemUser.objects.get(username = username)
        sklad_user = Rabotnik(user=user, order_sum = order_sum)
        sklad_user.save()
        return HttpResponseRedirect(reverse('remontnikUserDataIndex'))

    @login_required(login_url='authIndex')
    def remontnikUserUpdateData(request):
        id = request.POST['update_id']
        try:
            a = systemUser.objects.get(id=id)
        except:
            raise Http404("Неверный id")

        number = request.POST['number']
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        birthday = request.POST['birthday']
        contact_number = request.POST['contact_number']
        a.number = number
        a.username = username
        a.first_name = first_name
        a.last_name = last_name
        a.password = password
        a.birhtday = birthday
        a.contact_number = contact_number
        a.user_base.username = username
        a.user_base.password = make_password(password)
        a.user_base.save()
        a.save()
        return HttpResponseRedirect(reverse('remontnikUserDataIndex'))

    @login_required(login_url='authIndex')
    def remontnikDeleteUserData(request):
        id = request.POST['remove_id']
        try:
            a = systemUser.objects.get( id = id )
        except:
            raise Http404("Запись не найдена")
        Rabotnik.objects.get(user=a).delete()
        user_base = a.user_base
        Rabotnik.objects.filter(id=id).delete()
        user_base.delete()
        a.delete()
        return HttpResponseRedirect(reverse('remontnikUserDataIndex'))

class systemUser_view(View):
    @login_required(login_url='authIndex')
    def systemAdminUserIndex(request):
        #users = systemUser.objects.all().filter(position="Работник")
        users = systemUser.objects.values().filter(position="Админ")
        res = []
        res.append("id")
        res.append("Номер")
        res.append("Логин")
        res.append("Имя")
        res.append("Фамилия")
        res.append("Пароль")
        res.append("Дата рождения")
        res.append("Телефон")
        res.append("Количество бэкапов")
        res.append("Последний бэкап")
        data = list(users)
        for item in data:
            adm = Administrator.objects.get(user_id = item['id'])
            item['sum'] = adm.dbbackup_sum
            item['last'] = adm.dbbackup_last
        return render(request, 'skladApp/systemUserDataTable.html', {'data_table': data, 'titles': res})

    @login_required(login_url='authIndex')
    def systemUserAddData(request):
        number = request.POST['number']
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        birthday = request.POST['birthday']
        contact_number = request.POST['contact_number']
        backup_sum = 0
        base_user = User(username=username, password = make_password(password))
        base_user.save()
        base_user = User.objects.get(username=username)
        user = systemUser(user_base=base_user, number=number, username=username, first_name=first_name, last_name=last_name, password=password, position="Админ", birhtday=birthday, contact_number=contact_number)
        user.save()
        user = systemUser.objects.get(username = username)
        admin = Administrator(user=user, dbbackup_sum = backup_sum)
        admin.save()
        return HttpResponseRedirect(reverse('adminUserDataIndex'))

    @login_required(login_url='authIndex')
    def systemUserUpdateData(request):
        id = request.POST['update_id']
        try:
            a = systemUser.objects.get(id=id)
        except:
            raise Http404("Неверный id")

        number = request.POST['number']
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        birthday = request.POST['birthday']
        contact_number = request.POST['contact_number']
        a.number = number
        a.username = username
        a.first_name = first_name
        a.last_name = last_name
        a.password = password
        a.birhtday = birthday
        a.contact_number = contact_number
        a.user_base.username = username
        a.user_base.password = make_password(password)
        a.user_base.save()
        a.save()
        return HttpResponseRedirect(reverse('adminUserDataIndex'))

    @login_required(login_url='authIndex')
    def systemUserDeleteUserData(request):
        id = request.POST['remove_id']
        try:
            a = systemUser.objects.get( id = id )
        except:
            raise Http404("Запись не найдена")
        Administrator.objects.get(user=a).delete()
        user_base = a.user_base
        Administrator.objects.filter(id=id).delete()
        user_base.delete()
        a.delete()
        return HttpResponseRedirect(reverse('adminUserDataIndex'))

class dbbackup_view(View):
    @login_required(login_url='authIndex')
    def dbbackupIndex(request):
        db = Dbbackup.objects.values()
        res = []
        res.append("id")
        res.append("Номер")
        res.append("Название")
        res.append("Дата")
        data = db
        return render(request, 'skladApp/dbdackupDataTable.html', {'data_table': data, 'titles': res})

    @login_required(login_url='authIndex')
    def dbBackupAddData(request):
        number = request.POST['number']
        name = request.POST['name']
        final_name = number + "_" + name + ".dump"
        user = User.objects.get(username=request.user.username)
        dump = Dbbackup(number=number, name=final_name)
        dump.save()
        if not user.is_superuser:
            sys_user = systemUser.objects.get(user_base=user)
            admin = Administrator.objects.get(user=sys_user)
            admin.add_dbbackup(dump)
            admin.save()
        return HttpResponseRedirect(reverse('dbbackupIndex'))

    @login_required(login_url='authIndex')
    def dbBackupDeleteData(request):
        id = request.POST['remove_id']
        try:
            a = Dbbackup.objects.get(id=id)
        except:
            raise Http404("Запись не найдена")
        Dbbackup.objects.filter(id=id).delete()
        return HttpResponseRedirect(reverse('dbbackupIndex'))

class proizvodstvo_view(View):
    @login_required(login_url='authIndex')
    def proizvIndex(request):
        proizv = Proizvodstvo.objects.values()
        res = []
        res.append("id")
        res.append("Адрес")
        data = proizv
        if (res == []) | (data == []):
            return HttpResponse("Нет данных")
        return render(request, 'skladApp/proizvodstvoDataTable.html', {'data_table' :data  , 'titles' : res})

    @login_required(login_url='authIndex')
    def ProizvAddData(request):
        adress = request.POST['adress']
        a = Proizvodstvo(adress=adress)
        a.save()
        return HttpResponseRedirect(reverse('proizvIndex'))

    @login_required(login_url='authIndex')
    def ProizvDeleteData(request):
        id = request.POST['remove_id']
        try:
            a = Proizvodstvo.objects.get( id = id )
        except:
            raise Http404("Запись не найдена")
        Proizvodstvo.objects.filter(id=id).delete()
        return HttpResponseRedirect(reverse('proizvIndex'))

    @login_required(login_url='authIndex')
    def ProizvUpdateData(request):
        id = request.POST['update_id']
        try:
            a = Proizvodstvo.objects.get( id = id)
        except:
            raise Http404("Неверный id")

        adress = request.POST['adress']
        a.adress = adress
        a.save()
        return HttpResponseRedirect(reverse('proizvIndex'))

    @login_required(login_url='authIndex')
    def RefreshProizvTable(request):
        return HttpResponseRedirect(reverse('proizvIndex'))

class sklad_view(View):
    @login_required(login_url='authIndex')
    def skladIndex(request):
        s = Sklad.objects.values()
        res = []
        res.append("id")
        res.append("Адрес")
        res.append("Площадь склада")
        data = s
        if (res == []) | (data == []):
            return HttpResponse("Нет данных")
        return render(request, 'skladApp/skladDataTable.html', {'data_table': data, 'titles': res})

    @login_required(login_url='authIndex')
    def RefreshSkladTable(request):
        return HttpResponseRedirect(reverse('skladIndex'))

    @login_required(login_url='authIndex')
    def SkladAddData(request):
        adress = request.POST['adress']
        square = request.POST['square']
        a = Sklad(adress=adress, square=square)
        a.save()
        return HttpResponseRedirect(reverse('skladIndex'))

    @login_required(login_url='authIndex')
    def SkladDeleteData(request):
        id = request.POST['remove_id']
        try:
            a = Sklad.objects.get( id = id )
        except:
            raise Http404("Запись не найдена")
        Sklad.objects.filter(id=id).delete()
        return HttpResponseRedirect(reverse('skladIndex'))

    @login_required(login_url='authIndex')
    def SkladUpdateData(request):
        id = request.POST['update_id']
        try:
            a = Sklad.objects.get( id = id)
        except:
            raise Http404("Неверный id")

        adress = request.POST['adress']
        square = request.POST['square']
        a.adress = adress
        a.square = square
        a.save()
        return HttpResponseRedirect(reverse('skladIndex'))

class Auth_view(View):
    def AuthIndex(request):
        return render(request, 'auth.html')

    def Auth(request):
        login = request.POST['u']
        password = request.POST['p']
        user = auth.authenticate(username=login, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('navigate'))
        else:
            #return HttpResponse(user)
            return HttpResponseRedirect(reverse('authIndex'))

    @login_required(login_url='authIndex')
    def NavigateUser(request):
        try:
            base_user_id = User.objects.get(username = request.user.username)
            sys_user = systemUser.objects.get(user_base = base_user_id)
        except:
            return HttpResponseRedirect(reverse('systemAdminIndex'))
        if sys_user.position == "Склад":
            return HttpResponseRedirect(reverse('skladAdminIndex'))
        elif sys_user.position == "Работник":
            return HttpResponseRedirect(reverse('rabotnikIndex'))
        elif sys_user.position == "Админ":
            return HttpResponseRedirect(reverse('systemAdminIndex'))

    def Logout(request):
        auth.logout(request)
        return HttpResponseRedirect(reverse('authIndex'))





