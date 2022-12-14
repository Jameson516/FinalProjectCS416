from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('contact/', views.contact, name='contact'),
    path('category/', views.view_category, name='view_category'),
    path('add', views.create_category, name='create_category'),
    path('update/<int:category_id>', views.update_category, name='update_category'),
    path('delete/<int:category_id>', views.delete_category, name='delete_category'),
]
