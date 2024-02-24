"""
URL configuration for MODEL_RELATION project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from ONE_TO_ONE.views import *
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('sign_up/', sign_up, name='sign_up'),
    path('profile/', profile, name='profile'),
    path('change_profile/', change_profile, name='change_profile'),
    path('user_logout/',user_logout,name='user_logout')
    # path('user_login/', login_user, name='login_user'),
]+static(settings.MEDIA_URL ,document_root=settings.MEDIA_ROOT)
