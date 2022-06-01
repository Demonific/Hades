from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from . import models

class OrderListView(ListView):
	model = models.Order

class OrderDetailView(DetailView):
	model = models.Order

class OrderUpdateView(UpdateView):
	model = models.Order
	fields = "__all__"
	success_url = "/"

class OrderDeleteView(DeleteView):
	model = models.Order
	success_url = "/"

class OrderCreateView(CreateView):
	model = models.Order
	fields = "__all__"
	success_url = "/"
