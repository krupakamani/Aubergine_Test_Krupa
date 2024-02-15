from django.urls import path
from .views import *

urlpatterns = [
    path('blog_detail',BlogDetail.as_view(), name='blog-detail'),
    path("blog_filter",BlogFilter.as_view(), name='blog-filter')
]

'''
This URL for create blog
http://127.0.0.1:8000/blog/blog_detail
'''

'''
This URL for blog listing & pagination
http://127.0.0.1:8000/blog/blog_detail?page_size=2&page_index=1
'''


'''
This URL for Blog filtering & pagination
For Category: http://127.0.0.1:8000/blog/blog_filter?category=category 1&page_size=10&page_index=1
For Tag: http://127.0.0.1:8000/blog/blog_filter?tag=tag 1&page_size=10&page_index=1
'''