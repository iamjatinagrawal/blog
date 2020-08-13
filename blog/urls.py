from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import (PostListView, PostDetailView,
                    ContactFormCreateView, SearchPostListView,
                    IndexPostListView)

urlpatterns = [

                  path('', IndexPostListView.as_view(), name='index'),
                  path('search/', SearchPostListView.as_view(), name='search-post-list'),
                  path('blog/<q>', PostListView.as_view(), name='django-post-list'),
                  path('blog/<q>', PostListView.as_view(), name='python-post-list'),
                  path('blog/<q>', PostListView.as_view(), name='excel-post-list'),
                  path('blog/<q>', PostListView.as_view(), name='howto-post-list'),
                  path('post/<pk>', PostDetailView.as_view(), name='post-detail'),
                  path('contact/', ContactFormCreateView.as_view(), name='contact-page'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
