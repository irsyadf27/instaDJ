"""instadj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from rest_framework_swagger.views import get_swagger_view
from rest_framework.authtoken.views import ObtainAuthToken

schema_view = get_swagger_view(title='InstaDJ API')


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/', include('post.urls')),
    url(r'^api/v1/', include('profile.urls')),
    url(r'^api/v1/auth_token/$', ObtainAuthToken.as_view()),
    url(r'^api/v1/docs/$', schema_view)
]
