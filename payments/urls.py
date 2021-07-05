from django.urls import path

from . import views

urlpatterns = [
    path('payments/', views.ProductView.as_view(), name='payments'),
    path('config/', views.stripe_config, name ='checkout'),
    path('create-checkout-session/', views.create_checkout_session),
]