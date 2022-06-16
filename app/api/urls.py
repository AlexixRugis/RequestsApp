from django.urls import path
from app.api.views.account.LoginView import LoginView
from app.api.views.account.LogoutView import LogoutView
from app.api.views.account.MyAccountView import MyAccountView
from app.api.views.parts.AddPartRequestsView import AddPartRequestsView
from app.api.views.parts.RepairPartsListView import *
from app.api.views.repair_requests.AcceptRequestView import AcceptRequestView
from app.api.views.repair_requests.AccountRepairTasksView import AccountRepairTasksView
from app.api.views.repair_requests.AvailableRepairRequestsView import AvailableRepairRequestsView
from app.api.views.repair_requests.CompleteTaskView import CompleteTaskView
from app.api.views.repair_requests.CompletedRepairTaskDetailView import CompletedRepairTaskDetailView
from app.api.views.repair_requests.CompletedRepairTasksView import CompletedRepairTasksView
from app.api.views.repair_requests.RepairRequestDetailView import RepairRequestDetailView
from app.api.views.repair_requests.RepairTaskDetailView import RepairTaskDetailView
from app.api.views.account.IsAuthenticatedView import IsAuthenticatedView



urlpatterns = [
    # вход
    path("login/", LoginView.as_view()),
    # выход
    path ("logout/", LogoutView.as_view()),
    # личный кабинет    
    path("account/", MyAccountView.as_view()),
    path("is_authenticated/", IsAuthenticatedView.as_view()),

    # просмотр всех доступных заявок
    path("requests/", AvailableRepairRequestsView.as_view()),
    path("requests/<int:pk>/", RepairRequestDetailView.as_view()),
    
    # отклик на заявку
    path("requests/<int:pk>/accept/", AcceptRequestView.as_view()),

    # просмотр своих заявок
    path("tasks/", AccountRepairTasksView.as_view()),
    path("tasks/completed/", CompletedRepairTasksView.as_view()),
    path("tasks/<int:pk>/", RepairTaskDetailView.as_view()),
    path("tasks/completed/<int:pk>/", CompletedRepairTaskDetailView.as_view()),

    # завершение заявки
    path("tasks/<int:pk>/complete/", CompleteTaskView.as_view()),

    # просмотр доступных деталей
    path("repair_parts/", RepairPartsListView.as_view()),

    # прикрепление деталей к заявке
    path("tasks/<int:pk>/add_parts/", AddPartRequestsView.as_view())
]