from django.conf.urls import url
from blog_app import views

urlpatterns = [
        url(r'^$',views.PostListView.as_view(),name='post_list'),
        url(r'^about/$',views.AboutView.as_view(),name='about'),
        url(r'^post/(?P<pk>\d+)$', views.PostDetailView.as_view(), name='post_detail'),
        url(r'^post/new/$',views.CreateView.as_view(),name='post_new'),
        url(r'^post/(?P<pk>\d+)/edit/$', views.PostUpdateView.as_view(), name='post_edit'),
        url(r'^post/(?P<pk>\d+)/remove/$', views.DeleteView.as_view(), name='post_remove'),
        url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish.as_view(), name='post_publish'),
        url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish.as_view(), name='post_publish'),
        url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post.as_view(), name='add_comment_to_post'),
        url(r'^post/(?P<pk>\d+)/approve/$', views.comment_approve.as_view(), name='comment_approve'),
        url(r'^post/(?P<pk>\d+)/publish/$', views.comment_remove.as_view(), name='comment_remove'),



]
