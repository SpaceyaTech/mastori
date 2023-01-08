from rest_framework import serializers

from blog.models import Stori

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stori
        fields = '__all__'