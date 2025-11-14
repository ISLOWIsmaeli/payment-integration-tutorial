from django.urls import path, re_path
from . import views
urlpatterns = [
    path("payments/<int:pk>/", views.payments_home, name="payments-home")
]