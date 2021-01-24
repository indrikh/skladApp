from django.urls import path,include
from django.contrib import admin


from . import views

urlpatterns = [
    path('skladAdminMenu', views.skladAdminIndex, name = 'skladAdminIndex'),
    path('sklad/', views.sklad_view.skladIndex, name = 'skladIndex'),
    path('detals/', views.detal_view.detalIndex, name = 'detalIndex'),
    path('proizv/', views.proizvodstvo_view.proizvIndex, name = 'proizvIndex'),
    path('stanoks/', views.stanok_view.stanokIndex, name = 'stanokIndex'),
    path('updateTable/', views.stanok_view.updateTable, name ='refresh'),
    path('stanoks/add_data', views.stanok_view.StanoksAddData, name='stanoksAddData'),
    path('stanoks/remove_data', views.stanok_view.DeleteData, name='stanoksRemoveData'),
    path('stanoks/update_data', views.stanok_view.UpdateStanoksData, name='stanoksUpdateData'),
    path('proizv/add_data', views.proizvodstvo_view.ProizvAddData, name='proizvAddData'),
    path('proizv/remove_data', views.proizvodstvo_view.ProizvDeleteData, name='proizvRemoveData'),
    path('proizv/update_data', views.proizvodstvo_view.ProizvUpdateData, name='proizvUpdateData'),
    path('proizv/refresh', views.proizvodstvo_view.RefreshProizvTable, name='proizvRefresh'),
    path('sklad/add_data', views.sklad_view.SkladAddData, name='skladAddData'),
    path('sklad/remove_data', views.sklad_view.SkladDeleteData, name='skladRemoveData'),
    path('sklad/update_data', views.sklad_view.SkladUpdateData, name='skladUpdateData'),
    path('sklad/refresh', views.sklad_view.RefreshSkladTable, name='skladRefresh'),
    path('detal/add_data', views.detal_view.DetalAddData, name='detalAddData'),
    path('detal/remove_data', views.detal_view.DetalDeleteData, name='detalRemoveData'),
    path('detal/update_data', views.detal_view.DetalUpdateData, name='detalUpdateData'),
    path('detal/refresh', views.detal_view.RefreshDetalTable, name='detalRefresh'),
    path('rabotnikMenu/', views.rabotnikIndex, name='rabotnikIndex'),
    path('rabotnikMenu/nakls', views.rabotnikNaklsIndex, name='rabotnikNaklsIndex'),
    path('rabotnikMenu/AddNakls', views.AddNakl, name='rabotnikAddNakls'),
    path('login', views.Auth_view.AuthIndex, name='authIndex'),
    path('auth/', views.Auth_view.Auth, name='authUser'),
    path('navigate', views.Auth_view.NavigateUser, name='navigate'),
    path('', views.Auth_view.AuthIndex, name='main'),
    path('logout', views.Auth_view.Logout, name='logout'),
    path('systemAdminMenu', views.systemAdminIndex, name='systemAdminIndex'),
    path('systemAdminMenu/skladUsers', views.skladAdmin_view.skladUserIndex, name='skladUserDataIndex'),
    path('systemAdminMenu/skladUsers/AddUser', views.skladAdmin_view.SkladUserAddData, name='skladUserAddDataIndex'),
    path('systemAdminMenu/skladUsers/DeleteUser', views.skladAdmin_view.SkladDeleteUserData, name='skladUserDeleteDataIndex'),
    path('systemAdminMenu/skladUsers/UpdateUser', views.skladAdmin_view.SkladUserUpdateData, name='skladUserUpdateDataIndex'),
    path('systemAdminMenu/rabotnikUsers', views.remontnikUser_view.remontnikUserIndex, name='remontnikUserDataIndex'),
    path('systemAdminMenu/rabotnikUsers/AddData', views.remontnikUser_view.remontnikUserAddData, name='remontnikAddUserDataIndex'),
    path('systemAdminMenu/rabotnikUsers/UpdateData', views.remontnikUser_view.remontnikUserUpdateData, name='remontnikUpdateUserDataIndex'),
    path('systemAdminMenu/rabotnikUsers/DeleteData', views.remontnikUser_view.remontnikDeleteUserData, name='remontnikDeleteUserDataIndex'),
    path('systemAdminMenu/systemAdmins', views.systemUser_view.systemAdminUserIndex, name='adminUserDataIndex'),
    path('systemAdminMenu/systemAdmins/AddData', views.systemUser_view.systemUserAddData, name='adminUserAddDataIndex'),
    path('systemAdminMenu/systemAdmins/UpdateData', views.systemUser_view.systemUserUpdateData, name='adminUserUpdateDataIndex'),
    path('systemAdminMenu/systemAdmins/DeleteData', views.systemUser_view.systemUserDeleteUserData, name='adminUserDeleteDataIndex'),
    path('systemAdminMenu/Dbbackup', views.dbbackup_view.dbbackupIndex, name='dbbackupIndex'),
    path('systemAdminMenu/Dbbackup/Create', views.dbbackup_view.dbBackupAddData, name='dbbackupAddIndex'),
    path('systemAdminMenu/Dbbackup/Delete', views.dbbackup_view.dbBackupDeleteData, name='dbbackupDeleteIndex'),




]