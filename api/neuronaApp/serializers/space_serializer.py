from rest_framework import serializers
from ..models import Spaces, SpacesMembers, SpacesAdmins
from ..models import Privacy
 
class SpaceSerializer(serializers.ModelSerializer):
    joined = serializers.SerializerMethodField()
    is_admin = serializers.SerializerMethodField()

    class Meta:
        model = Spaces
        fields = [
            'id',
            'name',
            'about',
            'image_url',
            'joined',
            'is_admin',
        ]

    def get_joined(self, obj):
        return SpacesMembers.objects.filter(user_id=self.context.id, space_id=obj.id).exists()

    def get_is_admin(self, obj):
        return SpacesAdmins.objects.filter(user_id=self.context.id, space_id=obj.id).exists()
