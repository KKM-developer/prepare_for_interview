from django.contrib import admin
from django.urls import path
from .views import index, goods_list, GoodsList

urlpatterns = [
    path('', goods_list),
    path('goods_cbv/', GoodsList.as_view()),
]
