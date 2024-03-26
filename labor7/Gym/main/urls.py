from django.urls import path
from .views import get_page, add_client
 
urlpatterns = [
	path("", get_page, name="form"),
    path('add/', add_client, name='add_client')
]
 
