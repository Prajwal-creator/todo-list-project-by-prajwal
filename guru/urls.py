"""
URL configuration for guru project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from demo.views  import loging ,signup ,amd ,home ,delete_task
from django.conf.urls.static import static
from django.conf import  settings 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',loging,name="dock"),
    path('signup/',signup,name="sign"),
    path('am/',amd,name="am"),
    path('edit/<int:srno>/',amd,name="amd"),
    path('home/',home,name="home"),
    path('deletetask/<int:srno>',delete_task,name="homer"),
]
urlpatterns  += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)