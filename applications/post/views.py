from rest_framework import generics
from applications.post.models import *
from applications.post.serializers import *
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from applications.post.permissions import IsOwner
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from applications.feedback.models import *
from applications.feedback.serializers import RatingSerializers
class CustomPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10000




# class PostListAPIView(generics.ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializers

# class PostCreateAPIView(generics.CreateAPIView):
#     serializer_class = PostSerializers

# class PostUpdateAPIView(generics.UpdateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializers 
#     lookup_field = 'id'

# class PostDeleteAPIView(generics.DestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializers
#     lookup_field = 'id'

# class PostDetailAPIView(generics.RetrieveAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializers
#     lookup_field = 'id'


# class PostListCreateAPIVIew(generics.ListCreateAPIView):
#     permission_classes = [IsOwner]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializers
    # pagination_class = CustomPagination

    # filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # filterset_fields = ['owner', 'title']
    # search_fields = ['title']
    # ordering_fields = ['id']

#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)
#     # def get_queryset(self):
#     #     queryset = super().get_queryset()
#     #     # queryset = queryset.filter(owner=2)
#     #     filter_owner = self.request.query_params.get('owner')
#     #     if filter_owner:
#     #         queryset = queryset.filter(owner=filter_owner)
#     #     return queryset

#     def get_serializer_context(self):
    
#         return super().get_serializer_context()

# class PostAllAPIView(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [IsOwner]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializers

class PostModelViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    permission_classes = [IsOwner]
    pagination_class = CustomPagination

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['owner', 'title', 'favorites']
    search_fields = ['title']
    ordering_fields = ['id', 'owner']

    @action(methods=['POST'], detail=True)
    def like(self, request, pk, *args, **kwargs):
        user = request.user
        print(user)
        like_obj, _ = Like.objects.get_or_create(owner=user,post_id=pk)
        like_obj.is_like = not like_obj.is_like
        like_obj.save()
        status = 'liked'
        if not like_obj.is_like:
            status = 'unliked'
    
    

        return Response({'status': status})


    @action(methods=['POST'], detail=True)
    def rating(self, request, pk, *args, **kwargs):
        serializer = RatingSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)

        rating_obj, _ = Rating.objects.get_or_create(owner=request.user, post_id=pk)
        rating_obj.rating = serializer.data['rating']
        rating_obj.save()
        
        return Response('Ok!')
    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    # @action(methods=['POST'], detail=True)
    # def favorite(self, request, pk, *args, **kwargs):
    #     user = request.user
    #     print(user)
    #     fav_obj, _ = Favorite.objects.get_or_create(owner=user,post_id=pk)
    #     fav_obj.is_favorite = not fav_obj.is_favorite
    #     fav_obj.save()
    #     status = 'favorite'
    #     if not fav_obj.is_favorite:
    #         status = 'not favorite'

    #     return Response({'status': status})
    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)


class CreateImageAPIView(generics.CreateAPIView):
    queryset = PostImage.objects.all()
    serializer_class = PostImageSerializer
    permission_classes = [IsAuthenticated]

class CommentViewSet(ViewSet):
    def list(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


class CommentModeViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)