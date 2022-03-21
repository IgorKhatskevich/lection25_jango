from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name= 'index'),
    path('about/', views.about, name= 'about'),
    path('home/', views.home, name= 'home'),
    path('book_detail/<int:book_id>/', views.book_detail, name='book_detail'),
    path('review_detail/<int:review_id>/', views.review_detail, name='review_detail'),
    path('book_list/', views.book_list, name='book_list'),
    path('review_list/', views.review_list, name='review_list'),
    path('book_review_list/<int:book_id>/', views.book_review_list, name='book_review_list'),
    path('add_book/', views.add_book, name='add_book'),
    path("login_user/", views.login_user, name="login_user"),
    path("register_user/", views.register_user, name="register_user"),
    path("logout_user/", views.logout_user, name="logout_user"),
    path('add_review/<int:book_id>/', views.add_review, name='add_review'),
    path('delete_review/<int:review_id>/', views.delete_review, name='delete_review'),
    path('edit_review/<int:review_id>/', views.edit_review, name='edit_review'),
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),
]