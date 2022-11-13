from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from blog.models import Author
from post.models import BlogPost
from post.api.serializers import BlogPostSerializer


#create a blog post

@api_view(['POST',])
def create_post(request):
    user = Author.objects.get()
    blog_post = BlogPost(author=user) 

    if request.method == 'POST':
        serializer = BlogPostSerializer(blog_post,data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


#list a blog post

@api_view(['GET',])
def single_post_detail(request,pk):
    try:
        blog_post = BlogPost.objects.get(pk=pk)
    except BlogPost.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BlogPostSerializer(blog_post)
        return Response(serializer.data)


#list of posts

@api_view(['GET'])
def all_posts(request):
    
    # checking for the parameters from the URL
    if request.query_params:
        posts = BlogPost.objects.filter(**request.query_param.dict())
    else:
        posts = BlogPost.objects.all()
  
    # if there is something in posts else raise error
    if posts:
        serializer = BlogPostSerializer(posts,many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

#update a post

@api_view(['PUT',])
def update_post(request,pk):
    try:
        blog_post = BlogPost.objects.get(pk=pk)
    except BlogPost.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = BlogPostSerializer(blog_post,data=request.data)
        data= {}
        if serializer.is_valid():
            serializer.save()
            data['success']="update successful"
            return Response(data=data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#delete a post


@api_view(['DELETE',])
def delete_post(request,pk):
    try:
        blog_post = BlogPost.objects.get(pk=pk)
    except BlogPost.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        operation = blog_post.delete()
        data = {}
        if operation:
            data['success']="Post was deleted successfuly"
        else:
            data['failure']="delete failed"
        return Response(data=data)




        



