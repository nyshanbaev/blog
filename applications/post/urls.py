from django.urls import path, include
from applications.post.views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
# router.register('comments', CommentViewSet, basename='comment')
router.register('comment', CommentModeViewSet)
router.register('', PostModelViewSet)
urlpatterns = [
    # path('', PostListAPIView.as_view()),
    # path('create/', PostCreateAPIView.as_view()),
    # path('update/<int:id>/', PostUpdateAPIView.as_view()),
    # path('delete/<int:id>/', PostDeleteAPIView.as_view()),
    # path('detail/<int:id>/', PostDetailAPIView.as_view()),
    path('', include(router.urls)),
    # path('posts/', PostListCreateAPIVIew.as_view()),
    # path('<int:pk>/', PostAllAPIView.as_view()),
    path('add/image/', CreateImageAPIView.as_view()),
    # path('comments/', CommentViewSet.as_view({'get': 'list'}))
]