from rest_framework import serializers
from .models import Post, Comment
from .models import Like

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'post', 'user', 'created_at']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created_at', 'updated_at', 'like_count']

    def create(self, validated_data):
        # Automatically set the author to the logged-in user
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)
    

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'content', 'created_at', 'updated_at']  # Exclude 'author'

    def create(self, validated_data):
        # Automatically set the author to the logged-in user
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)