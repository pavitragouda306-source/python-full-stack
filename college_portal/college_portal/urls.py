
from django.contrib import admin
from django.urls import path
from Student import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('add/',views.forms,name='add'),
    path('add_form/',views.Student_form_dj,name='dj_form'),
    path('login/',views.user_login,name='login'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('logout/',views.user_logout,name='logout'),
    path('student/',views.Student_api,name='Student_api'),
]
