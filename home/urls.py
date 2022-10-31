from django.urls import path, include
from . import views
from rest_framework import routers

app_name = "home"

router = routers.DefaultRouter()
router.register(r'category', views.CategoryViewSet)

urlpatterns = [
    path('', include((router.urls, 'home.urls'))),
    path('', views.Home.as_view(), name='home'),
    path('products/', views.ProductListView.as_view()),
    path('products/<int:pk>/', views.ProductDetailView.as_view()),
    path('product/create/', views.ProductCreateView.as_view()),
    path('product/update/<int:pk>/', views.ProductUpdateView.as_view()),
    path('product/delete/<int:pk>/', views.ProductDeleteView.as_view()),
]
