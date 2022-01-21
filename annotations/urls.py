from django.urls import path

from . import views

app_name = 'annotations'
urlpatterns = [
	path('', views.index, name="index"),
	path('<int:annotation_id>/', views.detail, name='detail'),
	path('add/<str:spotify_id>/', views.add, name='add'),
	path('submit/', views.submit, name='submit'),
]