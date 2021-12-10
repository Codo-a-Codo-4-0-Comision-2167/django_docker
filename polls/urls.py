from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('read/<int:id>', views.read, name='read'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('create/', views.create, name='create'),
    path('update/<int:id>', views.update, name='update'),
]