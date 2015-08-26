from django.db.models import Q
from django.shortcuts import render
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from bookmarks.models import Bookmark
from bookmarks.serializers import BookmarkSerializer

class BookmarkListCreateAPIView(ListCreateAPIView):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('url', 'title')
    ordering_fields = ('id', 'url', 'title', 'bookmarked_at')


class BookmarkRetrieveUpdateDestroyAPIView(ListCreateAPIView):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
    lookup_field = 'bookmark_id'
