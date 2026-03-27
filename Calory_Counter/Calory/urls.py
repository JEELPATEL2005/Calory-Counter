from django.urls import path
from . import views

urlpatterns = [

    # auth
    path('', views.user_login, name="login"),
    path('register/', views.register, name="register"),
    path('logout/', views.user_logout, name="logout"),

    # profile
    path('profile/', views.profile, name="profile"),
    path('update-profile/', views.update_profile, name="update_profile"),

    # dashboard
    path('dashboard/', views.dashboard, name="dashboard"),

    # meal system
    path('meal/', views.meal_page, name="meal_page"),
    path('meal/add/', views.add_meal, name="add_meal"),
    path('meal/edit/<int:meal_id>/', views.edit_meal, name="edit_meal"),
    path('meal/delete/<int:meal_id>/', views.delete_meal, name="delete_meal"),


    # summary
    path('summary/', views.summary_page, name="summary_page"),

    # HTML reports
    path('report/7day/', views.html_report_7day, name="html_report_7day"),
    path('report/30day/', views.html_report_30day, name="html_report_30day"),

    # PDF reports
    path('report/pdf/7day/', views.pdf_report_7day, name="pdf_report_7day"),
    path('report/pdf/30day/', views.pdf_report_30day, name="pdf_report_30day"),

    # bot
    path('bot/', views.bot_page, name="bot_page"),
    path('bot/api/', views.bot_api, name="bot_api"),
]
