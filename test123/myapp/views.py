from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import *
from .helper import get_pagination
from .serializers import *
from rest_framework import status
from django.db import IntegrityError
from rest_framework.exceptions import ValidationError
from django.db.models import Q


class BlogDetail(APIView):
    '''
    This API handles blog creation
    '''
    def post(self, request):
        data = request.data
        tag_names = data.get("tag")
        
        try:
            category = Category.objects.get(category_name=data.get("category"))
        except:
            return Response({"status": False, "error": "Category not found"},status=status.HTTP_400_BAD_REQUEST,)
        
        tags = []
        for tag_name in tag_names:
            try:
                tag, created = Tag.objects.get_or_create(name=tag_name)
                tags.append(tag)
            except IntegrityError:
                raise ValidationError("Invalid tag data")

        blog_data = {
            "blog_name" : data.get("blog_name"),
            "category" : category,
        }
        try:
            new_blog = Blog.objects.create(**blog_data)
            new_blog.tag.set(tags)

            return Response({"status": True, "data": "Blog created successfully"},status=status.HTTP_201_CREATED,)
        except:
            return Response({"status": False, "error": "Something went wrong"}, status=status.HTTP_400_BAD_REQUEST,)
    
    '''
    This API handles blog listing & pagination .
    '''
    def get(self, request):
        data = Blog.objects.all()
        page_obj, total_page = get_pagination(request, data)

        try:
            if serializer := BlogSerializer(page_obj,many=True,):
                return Response(
                    {"status": True, "total_page":total_page, "data": serializer.data},
                    status=status.HTTP_200_OK,
                )
            return Response(
                {"status": False, "error": "Invalid request"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except Exception as e:
            return Response(
                {"status": False, "error": "Something went wrong"},
                status=status.HTTP_400_BAD_REQUEST,
            )


class BlogFilter(APIView):
    '''
    This API handles blog filtering for categories and tags.
    '''
    def get(self, request):

        category_name = request.GET.get('category', None)
        tag_name = request.GET.get('tag', None)

        blogs = Blog.objects.all()
        if category_name:
            blogs = Blog.objects.filter(category__category_name=category_name)

        if tag_name:
            blogs = Blog.objects.filter(tag__name=tag_name)
            
        page_obj, total_page = get_pagination(request, blogs)
        try:
            if serializer := BlogSerializer(page_obj,many=True,):
                return Response(
                    {"status": True, "total_page":total_page, "data": serializer.data},
                    status=status.HTTP_200_OK,
                )
            return Response(
                {"status": False, "error": "Invalid request"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except Exception as e:
            return Response(
                {"status": False, "error": "Something went wrong"},
                status=status.HTTP_400_BAD_REQUEST,
            )

