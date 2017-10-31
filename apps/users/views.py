from rest_framework import viewsets,mixins,pagination


from .serializer import UserProfileSerializer
from .models   import UserProfile

class Page(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 100


class UserProfileListViewset(mixins.ListModelMixin,viewsets.GenericViewSet):
     queryset  = UserProfile.objects.all()
     serializer_class = UserProfileSerializer
     pagination_class = Page