from django.urls import path
from app.api.views.account.LoginView import LoginView
from app.api.views.account.LogoutView import LogoutView
from app.api.views.account.MyAccountView import MyAccountView
from app.api.views.parts.RepairPartsListView import *
from app.api.views.repair_requests.AccountRepairTasksView import AccountRepairTasksView
from app.api.views.repair_requests.AvailableRepairRequestsView import AvailableRepairRequestsView



urlpatterns = [
    # вход
    path("login/", LoginView.as_view()),
    # выход
    path ("logout/", LogoutView.as_view()),
    # личный кабинет    
    path("account/", MyAccountView.as_view()),

    # просмотр всех доступных заявок
    path("requests/", AvailableRepairRequestsView.as_view()),
    
    # отклик на заявку

    # просмотр своих заявок
    path("tasks/", AccountRepairTasksView.as_view()),

    # завершение заявки

    # просмотр доступных деталей
    path("repair_parts/", RepairPartsListView.as_view()),
    # прикрепление деталей к заявке
]