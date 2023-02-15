from django.urls import path
from .views import UpdateView
from .views import UserLogoutView

urlpatterns = [
    path('', UpdateView.as_view(), name='home'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]