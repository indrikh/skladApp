from django.urls import path,include
from django.contrib import admin


from . import views

urlpatterns = [
    path('skladAdminMenu', views.skladAdminIndex, name = 'skladAdminIndex'),
    path('sklad/', views.skladIndex, name = 'skladIndex'),
    path('detals/', views.detalIndex, name = 'detalIndex'),
    path('proizv/', views.proizvIndex, name = 'proizvIndex'),
    path('stanoks/', views.stanokIndex, name = 'stanokIndex'),
    path('updateTable/', views.updateTable, name ='refresh'),
    path('stanoks/add_data', views.StanoksAddData, name='stanoksAddData'),
    path('stanoks/remove_data', views.DeleteData, name='stanoksRemoveData'),
    path('stanoks/update_data', views.UpdateStanoksData, name='stanoksUpdateData'),
    path('proizv/add_data', views.ProizvAddData, name='proizvAddData'),
    path('proizv/remove_data', views.ProizvDeleteData, name='proizvRemoveData'),
    path('proizv/update_data', views.ProizvUpdateData, name='proizvUpdateData'),
    path('proizv/refresh', views.RefreshProizvTable, name='proizvRefresh'),
    path('sklad/add_data', views.SkladAddData, name='skladAddData'),
    path('sklad/remove_data', views.SkladDeleteData, name='skladRemoveData'),
    path('sklad/update_data', views.SkladUpdateData, name='skladUpdateData'),
    path('sklad/refresh', views.RefreshSkladTable, name='skladRefresh'),
    path('detal/add_data', views.DetalAddData, name='detalAddData'),
    path('detal/remove_data', views.DetalDeleteData, name='detalRemoveData'),
    path('detal/update_data', views.DetalUpdateData, name='detalUpdateData'),
    path('detal/refresh', views.RefreshDetalTable, name='detalRefresh'),
    path('rabotnikMenu/', views.rabotnikIndex, name='rabotnikIndex'),
    path('rabotnikMenu/nakls', views.rabotnikNaklsIndex, name='rabotnikNaklsIndex'),
    path('rabotnikMenu/AddNakls', views.AddNakl, name='rabotnikAddNakls'),
    path('login', views.AuthIndex, name='authIndex'),
    path('auth/', views.Auth, name='authUser'),
    path('navigate', views.NavigateUser, name='navigate'),
    path('redirector', views.user_redirector, name='redirect'),
    path('', views.AuthIndex, name='main'),
    path('logout', views.Logout, name='logout'),
    path('systemAdminMenu', views.systemAdminIndex, name='systemAdminIndex'),
    path('systemAdminMenu/skladUsers', views.skladUserIndex, name='skladUserDataIndex'),
    path('systemAdminMenu/skladUsers/AddUser', views.SkladUserAddData, name='skladUserAddDataIndex'),
    path('systemAdminMenu/skladUsers/DeleteUser', views.SkladDeleteUserData, name='skladUserDeleteDataIndex'),
    path('systemAdminMenu/skladUsers/UpdateUser', views.SkladUserUpdateData, name='skladUserUpdateDataIndex'),
    path('systemAdminMenu/rabotnikUsers', views.remontnikUserIndex, name='remontnikUserDataIndex'),
    path('systemAdminMenu/rabotnikUsers/AddData', views.remontnikUserAddData, name='remontnikAddUserDataIndex'),
    path('systemAdminMenu/rabotnikUsers/UpdateData', views.remontnikUserUpdateData, name='remontnikUpdateUserDataIndex'),
    path('systemAdminMenu/rabotnikUsers/DeleteData', views.remontnikDeleteUserData, name='remontnikDeleteUserDataIndex'),
    path('systemAdminMenu/systemAdmins', views.systemAdminUserIndex, name='adminUserDataIndex'),
    path('systemAdminMenu/systemAdmins/AddData', views.systemUserAddData, name='adminUserAddDataIndex'),
    path('systemAdminMenu/systemAdmins/UpdateData', views.systemUserUpdateData, name='adminUserUpdateDataIndex'),
    path('systemAdminMenu/systemAdmins/DeleteData', views.systemUserDeleteUserData, name='adminUserDeleteDataIndex'),
    path('systemAdminMenu/Dbbackup', views.dbbackupIndex, name='dbbackupIndex'),
    path('systemAdminMenu/Dbbackup/Create', views.dbBackupAddData, name='dbbackupAddIndex'),
    path('systemAdminMenu/Dbbackup/Delete', views.dbBackupDeleteData, name='dbbackupDeleteIndex'),




]