from django.urls import path
from . import views

app_name="memories"
urlpatterns = [
    path('show_memories/',views.ShowMemories.as_view(), name='show_memories'),
    path('registermemory/',views.add_memory, name='registermemory'),
    path('like/',views.like, name='like'),
    
]