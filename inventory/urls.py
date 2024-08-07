from django.urls import path
from . import views

urlpatterns = [
    path('cars/', views.all_cars, name='all_cars'),
    path('cars/new/', views.add_new_car, name='add_new_car'),
    path('cars/<int:id>/', views.car_detail, name='car_detail'),
    path('car/<int:id>/edit/', views.car_edit, name='car_edit'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('', views.index, name='index')
] 