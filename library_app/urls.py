from django.urls import path ,include
from library_app import views
from library_app.views import (BookCreateView, BookDetailView, BookListView, BookUpdateView, BookDeleteView, )





app_name = 'app'

urlpatterns = [

    path('', views.index_page, name='index'),
    path('Book_create/', BookCreateView.as_view(), name='Book-create'),
    path('Book_list/', BookListView.as_view(), name='Book-list'),
    path('Book/<int:pk>/', BookDetailView.as_view(), name='Book-detail'),
    path('Book/<int:pk>/update/', BookUpdateView.as_view(), name='Book-update'),
    path('Book/<int:pk>/delete/', BookDeleteView.as_view(), name='Book-delete'),  
    
]
