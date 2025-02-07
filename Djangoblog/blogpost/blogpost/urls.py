from django.urls import path, include  
from django.contrib import admin
from django.urls import path
from .import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
    path('', views.home),
    path('about/', views.about)
]
