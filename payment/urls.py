from django.urls import path, re_path
from . import views
urlpatterns = [
    path("", views.payment_home, name="payment_home")
]
