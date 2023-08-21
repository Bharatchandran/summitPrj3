from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('interests/', views.InterestList.as_view(), name='interest_list'),
    path('interests/<int:pk>/update/', views.InterestUpdate.as_view(), name='interest_update'),
    path('interests/<int:pk>/delete/', views.InterestDelete.as_view(), name='interest_delete'),
    # path('groups/<int:pk>', views.GroupList.as_view(), name='group_list'),
    path('interests/<int:interest_id>/groups/', views.group_list, name='group_list'),
    path('interests/<int:interest_id>/groups/new', views.group_new, name='group_new'),
    path('interests/<int:interest_id>/groups/create', views.group_create, name='group_create'),
    path('interests/<int:id>/groups/<int:pk>/', views.group_detail, name='group_detail'),
    # path('interests/<int:id>/groups/<int:pk>/', views.GroupDetail.as_view(), name='group_detail'),
    path('interests/<int:id>/groups/<int:pk>/update/', views.GroupUpdate.as_view(), name='group_update'),
    path('interests/<int:id>/groups/<int:pk>/delete/', views.GroupDelete.as_view(), name='group_delete'),
]

