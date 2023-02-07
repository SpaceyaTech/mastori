from rest_framework import serializers

from blog.models import Stori


class BlogSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Stori
        fields = '__all__'
