from django.contrib import admin
from django.urls import path
from hades import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.OrderListView.as_view()),
    path('order/<int:pk>', views.OrderDetailView.as_view()),
    path('order/<int:pk>/update', views.OrderUpdateView.as_view()),
    path('new/', views.OrderCreateView.as_view()),
    path('order/<int:pk>/delete', views.OrderDeleteView.as_view()),
]
