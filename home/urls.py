from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('products/', views.ProductListView.as_view()),
    path('product/create/', views.ProductCreateView.as_view()),
    path('product/update/<int:pk>/', views.ProductUpdateView.as_view()),
    path('product/delete/<int:pk>/', views.ProductDeleteView.as_view()),
]
