from . import models
from django.views import generic


class OrderList(generic.ListView):
    model = models.Order
    template_name = 'index.html'


class OrderDetail(generic.DetailView):
    model = models.Order
