from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    # path('priority/', views.priority, name='index'),
    # path('error/', views.error, name='index'),
    path('Action/', views.Action.as_view()),
    # path('emergency/', views.emergency, name='index'),
    # path('belt/<int:pk>', views.belt, name='index'),
    # path('active/', views.active, name='index'),
]