from django.urls import path
from contact import views

app_name = 'contact'

urlpatterns = [
    #contact
    path('contact/<int:contact_id>/', views.contact, name='contact'),
    path('contact/<int:contact_id>/update/', views.update, name='update'),
    path('contact/<int:contact_id>/delete/', views.delete, name='delete'),
    path('contact/create/', views.create, name='create'),

    #user
    path('user/register/', views.register, name='register'),
    
    #agenda
    path('search/', views.search, name='search'),
    path('', views.index, name='index'),
]