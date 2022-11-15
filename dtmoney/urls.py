
from django.conf.urls import include
from django.contrib import admin
from django.urls import path

from rest_framework import routers

from transaction.api.viewsets import TransactionViewSet

router = routers.DefaultRouter()

router.register('transactions', TransactionViewSet, basename='Transaction')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
