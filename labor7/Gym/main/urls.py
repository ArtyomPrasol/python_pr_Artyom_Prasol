from django.urls import path, include
from .views import get_page, add_client, detail_client, update_client, ClientViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'ClientModel', ClientViewSet)

urlpatterns = [
	path("form", get_page, name="form"),
    path('add/', add_client, name='add_client'),
    path('client/<int:pk>/', detail_client, name='detail_client'),
    path('modif/', include(router.urls), name="modif_client"),
    path('upd/<int:pk>/', update_client, name='update_client')
]
 
