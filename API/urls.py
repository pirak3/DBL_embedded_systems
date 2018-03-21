from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('robot/', csrf_exempt(views.Robot.as_view())),
    # path('priority/', views.priority, name='index'),
    # path('error/', views.error, name='index'),
    # path('Action/', views.Action.as_view()),
    # path('emergency/', views.emergency, name='index'),
    # path('belt/<int:pk>', views.belt, name='index'),
    # path('active/', views.active, name='index'),
]
urlpatterns = format_suffix_patterns(urlpatterns)