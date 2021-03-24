from django.urls import path
from . import views

urlpatterns = [
    path('',views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'), 
    # django va a pasar un int con el nombre pk, este lo va a sacar de la url que ponga el usuario
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit', views.post_edit, name='post_edit')
]