from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('Robot/', csrf_exempt(views.RobotList.as_view())),
    path('Robot/<int:pk>/', csrf_exempt(views.RobotAdd.as_view())),
    path('Priority/', csrf_exempt(views.Priority.as_view())),
    path ('Error/', csrf_exempt(views.ErrorList.as_view()), name='index'),
    path('Action/', csrf_exempt(views.ActionList.as_view())),
    # path('emergency/', views.emergency, name='index'),
    # path('belt/<int:pk>', views.belt, name='index'),
    path('Active/<int:pk>/', csrf_exempt(views.ActiveList.as_view()), name='index'),
]
urlpatterns = format_suffix_patterns(urlpatterns)