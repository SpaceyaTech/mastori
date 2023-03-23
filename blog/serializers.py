from rest_framework import serializers

from accounts.models import Account
from blog.models import Stori, Comment, Category

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

class CategorySerializers(serializers.ModelSerializer)        :
    class Meta:
        model = Category
        fields = "__all__"
class BlogSerializer(serializers.ModelSerializer):
    comment = serializers.HyperlinkedRelatedField(many=True,view_name="comment-detail",read_only=True)
    # # category = serializers.CharField(source="category.name",read_only=True)
    class Meta:
        model = Stori
        exclude = ("slug",)
        depth = 1
