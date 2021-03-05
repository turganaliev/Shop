from django.urls import path

from distributor import views as product_views

urlpatterns = [
    path('products/', product_views.product_list_view),
]