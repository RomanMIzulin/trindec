from django.urls import path

from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('creation_thread', views.creation_thread, name='creation_thread'),
        path('asdf', views.creation, name = 'creation_thread_receive'),
        path('tredec',views.index,name='hui'),
        path('thread/<int:thread_id>', views.thread_num ),
]
