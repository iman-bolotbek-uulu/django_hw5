from django.urls import path
from . import views

urlpatterns = [
    path('', views.OrderList.as_view(), name='index'),
    path('<int:pk>/detail/', views.OrderDetail.as_view(template_name='detail.html'), name='detail'),
]