from django.urls import path
from . import views

# http://127.0.0.1:8000/cafeteria/

urlpatterns = [
    path("", views.all_drinks, name='all_drinks'),
    path("menu/", views.menu, name='menu'),
    path('<int:menu_id>/', views.menu_detail, name='menu_detail'),
    path("orders/", views.orders, name='oreders'),
    path("about/", views.about, name='about'),
    path("contact/", views.contact, name='contact'),
]
