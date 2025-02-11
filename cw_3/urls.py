from django.contrib import admin
from django.urls import path
from post import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('threads/', views.thread_list, name='threads'),
    path('threads/<int:id>/', views.thread_detail, name='thread_detail'),
]
