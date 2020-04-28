from django.urls import path, include
from perftest1.views import test_1, test_2

app_name = 'perftest1'

urlpatterns = [
    path('api/v1/testovi/<int:pk>/', test_1),
    path('api/v2/testovi/<int:pk>/', test_2),
]
