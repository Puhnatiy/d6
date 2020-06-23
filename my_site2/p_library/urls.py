from django.contrib import admin  
from django.urls import path  
from .views import AuthorEdit, AuthorList, author_create_many, books_authors_create_many, FriendEdit, FriendList, AuthorUpdate, AuthorDelete, BookEdit, BookList, BookUpdate, BookDelete
  
app_name = 'p_library'  
urlpatterns = [  
    path('author/create', AuthorEdit.as_view(), name='author_create'),  
    path('authors', AuthorList.as_view(), name='author_list'),
    path('author/<int:pk>/', AuthorUpdate.as_view(), name='author_edit'),
    path('books', BookList.as_view(), name='book_list'),
    path('book/<int:pk>/', BookUpdate.as_view(), name='book_edit'),
    path('author/<int:pk>/delete/', AuthorDelete.as_view(),
         name='author_delete'),
    path('author/create_many', author_create_many, name='author_create_many'),
    path('author_book/create_many', books_authors_create_many, name='author_book_create_many'),
    path('friend/create', FriendEdit.as_view(), name='friend_create'),  
    path('friends', FriendList.as_view(), name='friend_list'),    
]