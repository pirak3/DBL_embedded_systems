from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('robot/', csrf_exempt(views.RobotList.as_view())),
    # path('priority/', views.priority, name='index'),
    path ('Error/', csrf_exempt(views.ErrorList.as_view()), name='index'),
    path('Action/', csrf_exempt(views.ActionList.as_view())),
    # path('emergency/', views.emergency, name='index'),
    # path('belt/<int:pk>', views.belt, name='index'),
    # path('active/', views.active, name='index'),
]
urlpatterns = format_suffix_patterns(urlpatterns)