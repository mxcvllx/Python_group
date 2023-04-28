from django.contrib.auth.views import LogoutView
from django.urls import path

from account.views import custom_login, profile, RegisterView

app_name = "account"

urlpatterns = [
    #   path("login/", AccountLoginView.as_view(), name="login"),
    path("login/", custom_login, name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("profile/", profile, name="profile"),
    path("register/", RegisterView.as_view(), name="register")
]