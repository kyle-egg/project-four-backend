from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from .models import Gin, Comment
from .serializers import GinSerializer, CommentSerializer

class GinListView(ListCreateAPIView):
    ''' List View for /gins INDEX CREATE'''
    queryset = Gin.objects.all()
    serializer_class = GinSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

class GinDetailView(RetrieveUpdateDestroyAPIView):
    ''' Detail View for /gins/id SHOW UPDATE DELETE'''
    queryset = Gin.objects.all()
    serializer_class = GinSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

class CommentListView(APIView):
    ''' List View for /gins/ginId/comments CREATE comments'''

    permission_classes = (IsAuthenticated, )

    def post(self, request, gin_pk):
        request.data['gin'] = gin_pk
        request.data['owner'] = request.user.id
        created_comment = CommentSerializer(data=request.data)
        if created_comment.is_valid():
            created_comment.save()
            return Response(created_comment.data, status=status.HTTP_201_CREATED)
        return Response(created_comment.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class CommentDetailView(APIView):
    ''' DELETE COMMENT VIEW '''

    permission_classes = (IsAuthenticated, )

    def delete(self, _request, **kwargs):
        comment_pk = kwargs['comment_pk']
        try:
            comment_to_delete = Comment.objects.get(pk=comment_pk)
            comment_to_delete.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Comment.DoesNotExist:
            raise NotFound(detail='Comment Not Found')

class GinLikeView(APIView):
    ''' Adds likes to gins or removes if already liked '''

    permission_classes = (IsAuthenticated, )

    def post(self, request, gin_pk):
        try:
            gin_to_like = Gin.objects.get(pk=gin_pk)
        except Gin.DoesNotExist:
            raise NotFound()

        if request.user in gin_to_like.liked_by.all():
            gin_to_like.liked_by.remove(request.user.id)
        else:
            gin_to_like.liked_by.add(request.user.id)

        serialized_gin = GinSerializer(gin_to_like)

        return Response(serialized_gin.data, status=status.HTTP_202_ACCEPTED)
