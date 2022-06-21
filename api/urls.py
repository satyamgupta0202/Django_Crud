# 
from django.urls import path
from .import views

urlpatterns = [
    path('', views.apiOverview , name='apiOverview'),
    path('products-listsssss/', views.ShowAll,name="product-list"),
    path('product-detail/<int:pk>' ,views.ShowOne,name="product-detail"),
    path('product-create/' , views.CreateProduct,name="product-create"),
    path('product-update/<int:pk>' ,views.UpdateProduct,name="product-update"),
    path('product-delete/<int:pk>' ,views.DeleteProduct,name="product-delete")
]
