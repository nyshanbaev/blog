from rest_framework import serializers
from applications.post.models import *
from .models import User


class PostImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostImage 
        fields = '__all__'
        # exclude = ('post',)

class PostSerializers(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField()
    images = PostImageSerializer(many=True, read_only=True)
    owner = serializers.ReadOnlyField(source='owner.email')
    class Meta:
        model = Post 
        # fields = ('title',)
        fields = '__all__'
    
    # def to_representation(self, instance):
    #     # print(instance)
    #     representation = super().to_representation(instance)
    #     # print(representation)
    #     users = User.objects.all()
    #     representation['owner'] = instance.owner.email
    #     return representation
    
    def create(self, validated_data):
        validated_data['owner'] = self.context['request'].user


    #     return super().create(validated_data)
