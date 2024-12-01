from django.urls import path
from . import views
app_name = 'tasks'

urlpatterns = [
    path('', views.index, name='index'),
    path('task_list/', views.task_list_view, name='task_list'),
    path('create', views.create, name='create'),
    path('detail/<int:task_id>', views.detail, name='detail'),
    path('edit/<int:task_id>', views.edit, name='edit'),
    path('delete/<int:task_id>', views.delete, name='delete'),
    path('tasks/', views.task_list_view, name='task_list'),
    path('tasks/create/', views.create_task_view, name='create_task'),
    path('tasks/<pk>/', views.task_detail_view, name='task_detail'),
    path('tasks/<pk>/edit/', views.edit_task_view, name='edit_task'),
    path('tasks/<pk>/delete/', views.delete_task_view, name='delete_task'),
    path('login/', views.login_view, name='login'),
    path('detalles_cuenta/', views.detalles_cuenta, name='detalles_cuenta'),
    path('edit_account/', views.edit_account, name='edit_account'),
    path('edit_account/', views.edit_account, name='edit_account'),
    path('edit_password/', views.edit_password, name='edit_password'),
    path('delete_account/', views.delete_account, name='delete_account'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('edit_password/', views.edit_password, name='edit_password'),
    path('delete_account/', views.delete_account, name='delete_account'),
]
