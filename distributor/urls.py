from django.urls import path

from distributor import views

urlpatterns = [
    # path('products/', product_views.product_list_view),
    path('products/', views.ListCreateProductAPI.as_view()),
    path('categorys/', views.category_list_view),
    # path('categorys/', views.)
    path('tags/', views.tag_list_view),
]