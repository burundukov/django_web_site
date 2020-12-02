from django.contrib import admin
from django.urls import path, include
from users import views as userViews
from django.contrib.auth import views as authViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('top.urls')),
    path('registration/', userViews.register, name='registration'),
    path('auth/', authViews.LoginView.as_view(template_name='users/auth.html'), name='auth'),
    path('exit/', authViews.LogoutView.as_view(template_name='users/exit.html'), name='exit'),
    path('profile/', userViews.profile, name='profile'),
]
