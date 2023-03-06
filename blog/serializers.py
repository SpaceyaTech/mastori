from rest_framework import serializers

from blog.models import Stori

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stori
        fields = '__all__'


class StoriViewersSerializer(serializers.ModelSerializer):
    """Serializer of number of viewer of stori"""
    num_views = serializers.SerializerMethodField()

    class Meta:
        model = Stori
        fields = ('id', 'num_views')

    def get_num_views(self, obj):
        return obj.viewers.count()

