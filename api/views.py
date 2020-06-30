from api.serializers import GhostPostSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from api.models import GhostPost
from rest_framework.viewsets import ModelViewSet


class GhostPostViewSet(ModelViewSet):
    serializer_class = GhostPostSerializer
    basename = "ghostpost"
    queryset = GhostPost.objects.all()

    @action(detail=True, methods=['post'])
    def up_vote(self, request, pk=None):
        post = self.get_object()
        post.up_votes += 1
        post.save()
        return Response({"post": post.up_votes})

    @action(detail=True, methods=['post'])
    def down_vote(self, request, pk=None):
        post = self.get_object()
        post.down_votes += 1
        post.save()
        return Response({"post": post.down_votes})
