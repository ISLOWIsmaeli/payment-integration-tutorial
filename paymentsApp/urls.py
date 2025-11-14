from django.urls import path, re_path
from . import views
urlpatterns = [
    path("donation/<int:donation_id>/", views.donation, name="donation"),
    path('payment-success/<int:project_id>/', views.payment_successful, name='payment-success'),
    path('payment-failed/<int:project_id>/', views.payment_failed, name='payment-failed'),
    path('checkout/<int:project_id>/', views.create_paystack_checkout_session, name='donation-checkout'),
    path('webhook/paystack/', views.paystack_webhook),
]