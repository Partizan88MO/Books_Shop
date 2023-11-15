"""
URL configuration for proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from catalog import views as cat_views
from basket import views as bas_views 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/book/<int:pk>/', cat_views.BookDetail.as_view()),
    path('catalog/book/', cat_views.BookList.as_view()),
    path('catalog/book/create/', cat_views.BookCreate.as_view()), 
    path('catalog/book/update/<int:pk>/', cat_views.BookUpdate.as_view()),
    path('catalog/book/delete/<int:pk>/', cat_views.BookDelete.as_view()),
    path('catalog/publishing/<int:pk>/', cat_views.PublishingDetail.as_view()),
    path('catalog/publishing/', cat_views.PublishingList.as_view()),
    path('catalog/publishing/create/', cat_views.PublishingCreate.as_view()), 
    path('catalog/publishing/update/<int:pk>/', cat_views.PublishingUpdate.as_view()),
    path('catalog/publishing/delete/<int:pk>/', cat_views.PublishingDelete.as_view()),
    path('catalog/author/<int:pk>/', cat_views.AuthorDetail.as_view()),
    path('catalog/author/', cat_views.AuthorList.as_view()),
    path('catalog/author/create/', cat_views.AuthorCreate.as_view()), 
    path('catalog/author/update/<int:pk>/', cat_views.AuthorUpdate.as_view()),
    path('catalog/author/delete/<int:pk>/', cat_views.AuthorDelete.as_view()),
    path('catalog/anthology/<int:pk>/', cat_views.AnthologyDetail.as_view()),
    path('catalog/anthology/', cat_views.AnthologyList.as_view()),
    path('catalog/anthology/create/', cat_views.AnthologyCreate.as_view()), 
    path('catalog/anthology/update/<int:pk>/', cat_views.AnthologyUpdate.as_view()),
    path('catalog/anthology/delete/<int:pk>/', cat_views.AnthologyDelete.as_view()),
    path('catalog/genre/<int:pk>/', cat_views.GenreDetail.as_view()),
    path('catalog/genre/', cat_views.GenreList.as_view()),
    path('catalog/genre/create/', cat_views.GenreCreate.as_view()), 
    path('catalog/genre/update/<int:pk>/', cat_views.GenreUpdate.as_view()),
    path('catalog/genre/delete/<int:pk>/', cat_views.GenreDelete.as_view()),
    path('basket/order/<int:pk>/', bas_views.OrderDetail.as_view()),
    path('basket/order/', bas_views.OrderList.as_view()),
    path('basket/order/create/', bas_views.OrderCreate.as_view()), 
    path('basket/order/update/<int:pk>/', bas_views.OrderUpdate.as_view()),
    path('about-us/', bas_views.AboutUs.as_view()),  
    path('basket/order/delete/<int:pk>/', bas_views.OrderDelete.as_view()),
    path('basket/cart/', bas_views.cart),
]
