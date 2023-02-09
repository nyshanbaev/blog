from django.urls import path
from applications.post.views import *
urlpatterns = [
    # path('', PostListAPIView.as_view()),
    # path('create/', PostCreateAPIView.as_view()),
    # path('update/<int:id>/', PostUpdateAPIView.as_view()),
    # path('delete/<int:id>/', PostDeleteAPIView.as_view()),
    # path('detail/<int:id>/', PostDetailAPIView.as_view()),
    path('', PostListCreateAPIVIew.as_view()),
    path('<int:pk>/', PostAllAPIView.as_view()),
]