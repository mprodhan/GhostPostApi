from api.models import GhostPost
from rest_framework.serializers import ModelSerializer

class GhostPostSerializer(ModelSerializer):
    class Meta:
        model = GhostPost
        fields = (
            "id",
            "is_boast",
            "post",
            "up_votes",
            "down_votes",
            "submission",
            "total_votes"
        )