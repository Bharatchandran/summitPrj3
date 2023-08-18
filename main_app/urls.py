from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.home, name='home'),
    path('interests/', views.InterestList.as_view(), name='interest_index'),
    path('interests/<int:pk>/update/', views.InterestUpdate.as_view(), name='interest_update'),
    path('interests/<int:pk>/delete/', views.InterestDelete.as_view(), name='interest_delete'),
    path('interests/<int:id>/groups/', views.GroupsList.as_view(), name='group_index'),
    path('interests/<int:id>/groups/<int:pk>/', views.Groups.as_view(), name='group_detail'),
    path('interests/<int:id>/groups/<int:pk>/update/', views.GroupUpdate.as_view(), name='group_update'),
    path('interests/<int:id>/groups/<int:pk>/delete/', views.GroupDelete.as_view(), name='group_delete'),
]