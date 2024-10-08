"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path
from posts.views import text_response, html_response, post_list_view, post_detail_view


def home_view(request):
    return HttpResponse("Добро пожаловать на главную страницу!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('text/', text_response, name='text_response'),
    path('html/', html_response, name='html_response'),
    path('posts/', post_list_view),
    path('posts/<int:post_id>/', post_detail_view)

]
