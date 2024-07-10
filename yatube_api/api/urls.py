from rest_framework import routers
from django.urls import include, path

from api.views import (PostViewSet,
                       CommentViewSet,
                       GroupViewSet,
                       FollowViewSet)

router = routers.DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet, basename='comments'
)
router.register('groups', GroupViewSet, basename='groups')
router.register('follow', FollowViewSet, basename='follow')

v1_patterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls.jwt')),
]

urlpatterns = [
    path('v1/', include(v1_patterns)),
]
