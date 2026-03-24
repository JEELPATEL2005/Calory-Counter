from django.urls import path
from . import views

urlpatterns = [

    # Admin Logout
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    
    # Admin Dashboard
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    
    # Food Management
    path('foods/', views.manage_food, name='manage_foods'),
    path('foods/add/', views.add_food, name='add_food'),
    path('foods/edit/<int:food_id>/', views.edit_food, name='edit_food'),
    path('foods/delete/<int:food_id>/', views.delete_food, name='delete_food'),
    
    # User Management
    path('users/', views.manage_users, name='manage_users'),
    path('users/delete/<int:user_id>/', views.delete_user, name='delete_user'),
    
    # Admin Management
    path('admins/', views.manage_admins, name='manage_admins'),
    path('admins/add/', views.create_admin, name='add_admin'),
    path('admins/edit/<int:admin_id>/', views.edit_admin, name='edit_admin'),
    path('admins/delete/<int:admin_id>/', views.delete_admin, name='delete_admin'),
]
