from django.urls import path
from . import views
from .views import save_gist_to_local
urlpatterns = [
	path('', views.index, name="list"),
	path('update_task/<str:pk>/', views.updateTask, name="update_task"),
	path('delete_task/<str:pk>/', views.deleteTask, name="delete"),
    path('save-gist/<str:pk>/',save_gist_to_local, name= "save_gist_locally"),
	
]