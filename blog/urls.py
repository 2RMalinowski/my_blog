from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # Post views
    path('', views.post_list, name='post_list'),
    # path(views.PostListView.as_view(), name='post_list'),
    path('post/<int:year>/<int:month>/<int:day>/', views.post_detail, name='post_detail')
]
