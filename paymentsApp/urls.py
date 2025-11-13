from django.urls import path, re_path
from . import views
urlpatterns = [
    path("payment/", views.payment_home, name="payment_home")
]