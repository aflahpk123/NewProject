

from django.urls import path
from . import views

urlpatterns = [
    path('',views.add,name='add'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('listview/',views.TaskList.as_view(),name='listview'),
    path('detailview/<int:pk>/',views.TaskDetails.as_view(),name='detailview'),
    path('updateview/<int:pk>/',views.TaskUpdate.as_view(),name='updateview'),
    path('deleteview/<int:pk>/', views.TaskDelete.as_view(), name='deleteview'),
]