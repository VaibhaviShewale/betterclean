from django.urls import path

from betterclean import views
from .views import *

urlpatterns = [
    path('review', Review.as_view(), name='add_review'),
    path('review/post', create_review, name='create_review'),
    path('review/delete', create_review, name='delete_review'),
    path('all_reviews', all_reviews, name='all_reviews'),

    path('login', login_user, name='login'),
    path('register', register_user, name='register'),
    path('logout', logout_user, name='logout'),
]