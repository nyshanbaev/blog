from rest_framework import serializers
from applications.post.models import *
from .models import User
from applications.feedback.serializers import *
from django.db.models import Avg
# from applications.post.views import likers
class PostImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostImage 
        fields = '__all__'
        # exclude = ('post',)

class PostSerializers(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField()
    
    images = PostImageSerializer(many=True, read_only=True)
    likes = LikeSerializers(many=True, read_only=True)
    owner = serializers.ReadOnlyField(source='owner.email')

    
    
    class Meta:
        model = Post 
        # fields = ('title',)
        fields = '__all__'
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['likers'] = instance.likes.filter(is_like=True).count()


        representation['rating'] = instance.ratings.all().aggregate(Avg('rating'))['rating__avg']
        
        # for like in representation['likes']:
        #     if not like['is_like']:
        #         representation['likes'].remove(like)

        # raiting_result = 0
        # for rating in instance.ratings.all():
        #     raiting_result += rating.rating
        # if raiting_result:
        #     representation['rating'] = raiting_result / instance.ratings.all().count()
        # else:
        #     representation['rating'] = raiting_result
        
        return representation

    #     return instance
    # def to_representation(self, instance):
    #     # print(instance.likes.count())
    #     return self.likers + instance.likes.count()
    #     print('___________________________')
    #     users = User.objects.all()
    #     representation['owner'] = instance.owner.email
    #     return representation
    
    # def create(self, validated_data):
    #     validated_data['owner'] = self.context['request'].user


    #     return super().create(validated_data)
    def create(self, validated_data):
        post = Post.objects.create(**validated_data)
        request = self.context.get('request')
        data = request.FILES
        # for i in data.getlist('images'):
        #     PostImage.objects.create(post=post, image=i)
        
        image_objects = []
        for i in data.getlist('images'):
            image_objects.append(PostImage(post=post, image=i))
        PostImage.objects.bulk_create(image_objects)
        
        return post 
    
class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    
    class Meta:
        model = Comment
        fields = '__all__'

