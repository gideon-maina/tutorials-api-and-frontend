from rest_framework.serializers import ModelSerializer

from .models import Tutorial


class TutorialSerializer(ModelSerializer):
    class Meta:
        model = Tutorial
        fields = ['id', 'title', 'description', 'published']
