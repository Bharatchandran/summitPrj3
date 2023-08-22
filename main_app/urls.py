from django.urls import path
from . import views

urlpatterns = [
     path('', views.home, name='home'),

     # INTEREST URLS
     path('interests/', views.InterestList.as_view(), name='interest_list'),
     path('interests/create/', views.InterestCreate.as_view(), name='interest_create'),
     path('interests/<int:pk>/update/', views.InterestUpdate.as_view(), name='interest_update'),
     path('interests/<int:pk>/delete/', views.InterestDelete.as_view(), name='interest_delete'),
     # GROUP URLS
     path('interests/<int:interest_id>/groups/', views.group_list, name='group_list'),
     path('interests/<int:interest_id>/groups/new/', views.group_new, name='group_new'),
     path('interests/<int:interest_id>/groups/create/', views.group_create, name='group_create'),
     path('interests/groups/<int:group_id>/', views.group_detail, name='group_detail'),
     path('interests/groups/<int:pk>/update/', views.GroupUpdate.as_view(), name='group_update'),
     path('interests/groups/<int:pk>/delete/', views.GroupDelete.as_view(), name='group_delete'),

     # TOPIC URLS
     path('interests/groups/<int:group_id>/topics', views.topic_create, name='topic_create'),
     path('interest/groups/topic/<int:pk>/update', views.TopicUpdate.as_view(), name='topic_update'),
     path('interest/groups/topic/<int:pk>/delete', views.TopicDelete.as_view(), name='topic_delete'),
     path('interest/groups/topic/<int:pk>/update/', views.TopicUpdate.as_view(), name='topic_update'),
     path('interest/groups/topic/<int:pk>/delete/', views.TopicDelete.as_view(), name='topic_delete'),

     # POST URLS
     path('interest/groups/<int:group_id>/topic/<int:topic_id>/create', views.post_create, name='post_create'),
     path('interest/groups/topic/post/<int:pk>/update/', views.PostUpdate.as_view(), name='post_update'),
     path('interest/groups/topic/post/<int:pk>/delete', views.PostDelete.as_view(), name='post_delete'),
    #  path('interest/groups/topic/post/<int:post_id>/add_photo',views.add_photo, name='add_photo'),
]
