from rest_framework import serializers
from ..models import Spaces
from ..models import Privacy
 
class SpaceSerializer(serializers.ModelSerializer):
    privacy = serializers.ChoiceField(choices=[(tag.value, tag.name) for tag in Privacy])

    class Meta:
        model = Spaces
        fields = '__all__'