from django.urls import path
from . import views


urlpatterns = [
    path('', views.TemplCustomers.as_view(), name='customer'),
    path('<int:customer_id>/', views.TemplateInfoAboutOrders.as_view(), name='customer_orders'),
]
