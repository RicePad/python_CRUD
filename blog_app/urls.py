from django.conf.urls import url
from blog_app import views

urlpatterns = [
        url(r'^$',views.PostListView.as_view(),name='post_list'),
        url(r'^about/$',views.AboutView.as_view(),name='about'),
        url(r'^post/(?P<pk>\d+)$', views.PostDetailView.as_view(), name='post_detail'),
        url(r'^post/new/$',views.CreateView.as_view(),name='post_new'),
        url(r'^post/(?P<pk>\d+)/edit/$', views.PostUpdateView.as_view(), name='post_edit'),
        url(r'^post/(?P<pk>\d+)/remove/$', views.DeleteView.as_view(), name='post_remove'),


]
