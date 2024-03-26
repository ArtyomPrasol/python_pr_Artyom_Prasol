from django.urls import path
from .views import get_page, add_client, detail_client
 
urlpatterns = [
	path("", get_page, name="form"),
    path('add/', add_client, name='add_client'),
    path('client/<int:pk>/', detail_client, name='detail_client')
]
 
