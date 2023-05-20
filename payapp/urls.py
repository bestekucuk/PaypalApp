from django.urls import path
from payapp.views import PaymentListCreateView, PaymentDetailView

app_name = 'payapp'

urlpatterns = [
    path('payments/', PaymentListCreateView.as_view(), name='payment-list'),
    path('payments/<int:pk>/', PaymentDetailView.as_view(), name='payment-detail'),
]
