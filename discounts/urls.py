from django.urls import include, path
from rest_framework import routers
from . import views

app_name = 'discounts'

router = routers.DefaultRouter()
router.register(r'campaign', views.CampaignViewSet)
router.register(r'coupon', views.CouponViewSet)

urlpatterns = [
    path('', include((router.urls, 'discounts.urls'))),
]
