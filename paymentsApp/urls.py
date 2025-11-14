from django.urls import path, re_path
from . import views
urlpatterns = [
    path("payments/<int:pk>/", views.payments_home, name="payments-home"),
    path('payment-success/<int:project_id>/', views.payment_successful, name='payment-success'),
    path('payment-failed/<int:project_id>/', views.payment_failed, name='payment-failed'),
]