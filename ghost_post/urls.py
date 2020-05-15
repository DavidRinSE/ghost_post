from django.urls import path
from ghost_post import views

urlpatterns = [
    path('', views.index, name="homepage"),
    path('boasts/', views.boasts),
    path('roasts/', views.roasts),
    path('score/', views.score),
    path('newpost/', views.new_post_form),
    path('post/<int:id>/', views.post, name="post"),
    path('upvote/<int:id>/', views.upVote),
    path('downvote/<int:id>/', views.downVote)
]