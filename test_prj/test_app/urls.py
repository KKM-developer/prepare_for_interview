from django.contrib import admin
from django.urls import path
from .views import index, goods_list, GoodsList, ajax_test

urlpatterns = [
    path('', goods_list),
    path('ajax_test/', ajax_test),
    path('goods_cbv/', GoodsList.as_view()),
]
