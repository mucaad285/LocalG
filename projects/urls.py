
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('projects/', views.projects, name='projects'),
    path('single_project/<int:pk>/', views.single_project, name='single_project_id'),
    path('single_project/', views.single_project, name='single_project'),
    path('message_from_mayor/', views.message_from_mayor, name='message_from_mayor'),
    # path('add_comment/', views.add_comment, name='add_comment'),



]

