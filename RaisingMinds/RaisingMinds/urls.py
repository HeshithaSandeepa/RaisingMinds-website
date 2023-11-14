"""
URL configuration for RaisingMinds project.

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
from django.urls import path,include
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static
from users import views as userviews
from school_profile import views as school_profile_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('app.urls')),
    path('signup/',user_views.signup,name='signup'),
    path('login/',user_views.login,name='login'),
    path('forget-password/' , userviews.ForgetPassword , name="forget_password"),
    path('change-password/<token>/' ,userviews.ChangePassword , name="change_password"),
    path('activate/<uidb64>/<token>',user_views.activate,name='activate'),
    path('logout/',user_views.logout,name='logout'),
    path('schoolprofile/',school_profile_views.schoolprofile,name='schoolprofile')
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
