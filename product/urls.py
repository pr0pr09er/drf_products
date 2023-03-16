from django.urls import path
from views import ProductView

urlpatterns = [
    path('api/v1/', ProductView.as_view(), name="product_view"),
    path('api/v1/<int:pk>/', ProductView.as_view(), name="product_view"),
]
