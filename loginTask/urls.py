from django.contrib import admin
from django.urls import path, include
from tasks import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('account/', views.account_view, name='account'),
    path('account/edit/', views.edit_account_view, name='edit_account'),
    path('account/change_password/', views.change_password_view, name='change_password'),
    path('account/delete/', views.delete_account_view, name='delete_account'),
    path('tasks/', include('tasks.urls')),
    path('logout/', views.logout_view, name='logout'),
    path('detalles_cuenta/', views.detalles_cuenta, name='detalles_cuenta'),
]
