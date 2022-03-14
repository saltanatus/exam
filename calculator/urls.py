from django.urls import path
from . import views


urlpatterns = [
    path('main/', views.category_view, name='all_product'),
    path('main/resource/create/', views.create_view),
    path('main/resource/', views.resource_view, name='resource'),
    path('main/resource/<int:id>/delete/', views.delete_view, name='delete_view'),
    path('main/resource/<int:id>/update/', views.update_view, name='update_view'),
]