from .models import Post
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import PostSerializer, VoteSerializer
# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(detail=True, methods=['post'])
    def upVote(self, request, pk=None):
        try:
            post = Post.objects.get(id=pk)
            post.upVotes += 1
            post.save()
        except Post.DoesNotExist:
            return Response("Post not found")
        # check for does not exist error
        return Response("success")
    
    @action(detail=True, methods=['post'])
    def downVote(self, request, pk=None):
        try:
            post = Post.objects.get(id=pk)
            post.downVotes += 1
            post.save()
        except Post.DoesNotExist:
            return Response("Post not found")
        # check for does not exist error
        return Response("success")
