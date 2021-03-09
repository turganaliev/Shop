from django.urls import path

from distributor import views as product_views

urlpatterns = [
    path('products/', product_views.product_list_view),
    path('categorys/', product_views.category_list_view),
    path('tags/', product_views.tag_list_view),
]