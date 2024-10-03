from rest_framework import serializers

from blog.models import Stori, Comment, Category

class CommentSerializer(serializers.ModelSerializer):
    """comments serializer"""
    class Meta:
        model = Comment
        fields = ['id', 'account', 'stori', 'body']
        read_only_fields = ("account", "stori")


class CategorySerializers(serializers.ModelSerializer)        :
    "category serializers"
    class Meta:
        model = Category
        fields = "__all__"
        
        
class BlogSerializer(serializers.ModelSerializer):
    # comment = serializers.HyperlinkedRelatedField(many=True,view_name="comment-detail",read_only=True)
    # category = serializers.HyperlinkedRelatedField(view_name="category-detail",queryset=Category.objects.all())
    # comment = CommentSerializer(many=True,read_only=True)
    class Meta:
        model = Stori
        fields = ['id', 'title', 'slug', 'description', 'content', 'status', 'featured', 'category']
        read_only_fields = ("slug",)
    
        
      