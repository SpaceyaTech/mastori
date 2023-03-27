from rest_framework import serializers

from accounts.models import Account
from blog.models import Stori, Comment, Category

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ("user",)

class CategorySerializers(serializers.ModelSerializer)        :
    class Meta:
        model = Category
        fields = "__all__"
class BlogSerializer(serializers.ModelSerializer):
    comment = serializers.HyperlinkedRelatedField(many=True,view_name="comment-detail",read_only=True)
    category = serializers.HyperlinkedRelatedField(view_name="category-detail",queryset=Category.objects.all())

    class Meta:
        model = Stori
        fields = "__all__"
        read_only_fields = ("slug",)
        depth = 1
