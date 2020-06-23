from .models import Post
from rest_framework import serializers

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['isBoast', 'content', 'upVotes', 'downVotes', 'date', 'id']

class VoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['id']
