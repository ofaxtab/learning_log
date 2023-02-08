from django.urls import path
from .views import index, topics, topic


urlpatterns = [
    path('', index, name='index'),
    path('topics/', topics, name='topics'),
    path('topics/<int:topic_id>/', topic, name='topic'),

]
