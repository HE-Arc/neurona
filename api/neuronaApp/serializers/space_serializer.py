from rest_framework import serializers
from ..models import Spaces, SpacesMembers
from ..models import Privacy
 
class SpaceSerializer(serializers.ModelSerializer):
    joined = serializers.SerializerMethodField()

    class Meta:
        model = Spaces
        fields = [
            'id',
            'name',
            'about',
            'image_url',
            'joined'
        ]

    def get_joined(self, obj):
        return SpacesMembers.objects.filter(user_id=self.context.id, space_id=obj.id).exists()
