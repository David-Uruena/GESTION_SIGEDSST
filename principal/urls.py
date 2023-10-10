from django.contrib import admin
from django.urls import include, path
from principal.views import inicio_admin, logout_user
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('adm/', inicio_admin, name='inicio-admin'),
    path('', auth_views.LoginView.as_view(), name='inicio'),
    path('logout/', logout_user, name="logout"),
    
]
