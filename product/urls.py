#from xml.etree.ElementInclude import include
from django.urls import path, include
from product import views
#from tsuki.product.views import CategoryDetails
#from tsuki.product.views import LatestProductList

urlpatterns = [
    path('latest-products/', views.LatestProductList.as_view()),
    path('products/search/', views.search),
    path('products/<slug:category_slug>/<slug:product_slug>/', views.ProductDetails.as_view()),
    path('products/<slug:category_slug>/', views.CategoryDetails.as_view())
]