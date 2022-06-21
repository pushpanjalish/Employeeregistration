from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="index"),
    path('register',views.register,name="register"),
    path('profile',views.profile,name="profile"),
    path('logout',views.logoutpage,name="logoutpage"),
    path("password_reset", views.password_reset_request, name="password_reset")
]